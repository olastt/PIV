"""Сверка используемого Swagger: type/properties/items/$ref/nullable.

Считывает только YAML mapping-поля предоставленного файла. Примеры,
required-списки, formats и сложные композиции не валидируются; это не
полноценный OpenAPI validator. Реальные значения ответов не сохраняются.
"""

import re
from pathlib import Path


def read_contract(filename):
    root = {}
    stack = [(-1, root)]
    for line in Path(filename).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith(("#", "-")):
            continue
        match = re.match(r"^( *)([^:]+):(?:\s+(.*))?$", line)
        if not match:
            continue
        indent, key, value = len(match[1]), match[2].strip().strip("'\""), match[3]
        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if value is None or not value.strip():
            node = {}
            parent[key] = node
            stack.append((indent, node))
        else:
            value = value.strip().strip("'\"")
            parent[key] = True if value == "true" else False if value == "false" else value
    return root


def json_type(value):
    if value is None:
        return "null"
    return {dict: "object", list: "array", str: "string", int: "integer", bool: "boolean", float: "number"}.get(type(value), "unknown")


def schema_differences(value, schema, contract, path="$", depth=0):
    if depth > 30:
        raise ValueError("Слишком глубокая схема")
    if "$ref" in schema:
        ref = schema["$ref"]
        assert ref.startswith("#/"), "Поддерживаются только локальные ссылки Swagger"
        resolved = contract
        for part in ref[2:].split("/"):
            resolved = resolved[part]
        return schema_differences(value, resolved, contract, path, depth + 1)
    expected = schema.get("type")
    actual = json_type(value)
    if value is None and schema.get("nullable") is True:
        return []
    if expected and actual != expected and not (expected == "number" and actual == "integer"):
        return [{"path": path, "expected": expected, "actual": actual}]
    differences = []
    if isinstance(value, dict):
        for field, child in schema.get("properties", {}).items():
            if field in value:
                differences.extend(schema_differences(value[field], child, contract, f"{path}.{field}", depth + 1))
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            for field in value.keys() - schema.get("properties", {}).keys():
                differences.extend(schema_differences(value[field], additional, contract, f"{path}.*", depth + 1))
    elif isinstance(value, list) and isinstance(schema.get("items"), dict):
        for index, item in enumerate(value):
            differences.extend(schema_differences(item, schema["items"], contract, f"{path}[{index}]", depth + 1))
    return differences


def response_differences(raw, contract):
    path = raw.url.path.removeprefix("/api/v2")
    operation = contract["paths"].get(path, {}).get(raw.request.method.lower())
    if not operation:
        return [{"path": "$HTTP", "expected": "documented operation", "actual": "not documented"}]
    documented = operation.get("responses", {}).get(str(raw.status_code))
    differences = []
    if "security" in operation and "X-API-KEY" not in raw.request.headers and 200 <= raw.status_code < 300:
        differences.append({"path": "$security", "expected": "X-API-KEY required", "actual": "success without X-API-KEY"})
    if not documented:
        return differences + [{"path": "$HTTP.status", "expected": "documented response status", "actual": str(raw.status_code)}]
    content = documented.get("content", {})
    media_type = raw.headers.get("content-type", "").split(";", 1)[0].strip().lower()
    if media_type not in content:
        differences.append({"path": "$HTTP.Content-Type", "expected": list(content), "actual": media_type})
    schema = content.get("application/json", {}).get("schema")
    if schema:
        try:
            body = raw.json()
        except ValueError:
            return differences + [{"path": "$", "expected": "JSON", "actual": "invalid JSON"}]
        differences.extend(schema_differences(body, schema, contract))
        if path == "/medicalCards/vaccinations" and isinstance(body, dict):
            data = body.get("data")
            groups = data.get("vaccination", []) if isinstance(data, dict) else []
            for group_index, group in enumerate(groups):
                if isinstance(group, list):
                    for item_index, item in enumerate(group):
                        differences.extend(schema_differences(item, {"$ref": "#/components/schemas/VaccinationItem"}, contract,
                                                             f"$.data.vaccination[{group_index}][{item_index}]"))
        # После несовпадения контейнера отдельно исследуем поля элементов карты.
        if path == "/discountCard" and isinstance(body, dict) and isinstance(body.get("data"), dict):
            cards = body["data"].get("card", [])
            for index, card in enumerate(cards):
                differences.extend(schema_differences(card, {"$ref": "#/components/schemas/DiscountCardItem"}, contract, f"$.data.card[{index}]"))
    return differences
