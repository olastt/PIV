import httpx
import pytest

from qa_checks.swagger_contract import response_differences, schema_differences


@pytest.mark.parametrize("value,schema,expected", [
    ("1", {"type": "integer"}, True),
    (1, {"type": "boolean"}, True),
    (None, {"type": "string"}, True),
    (None, {"type": "string", "nullable": True}, False),
    ([], {"type": "object"}, True),
    ([[{"id": "1"}]], {"type": "array", "items": {"type": "object"}}, True),
    ({"extra": 1}, {"type": "object", "properties": {"optional": {"type": "string"}}}, False),
])
def test_contract_type_differences(value, schema, expected):
    assert bool(schema_differences(value, schema, {})) is expected


def test_nested_reference_detects_wrong_type_without_retaining_value():
    contract = {"components": {"schemas": {"Record": {"type": "object", "properties": {"number": {"type": "integer"}}}}}}
    differences = schema_differences({"number": "synthetic-private-number"}, {"$ref": "#/components/schemas/Record"}, contract)
    assert differences == [{"path": "$.number", "expected": "integer", "actual": "string"}]


def test_content_type_and_anonymous_success_are_both_detected():
    contract = {"paths": {"/endpoint": {"get": {"security": {}, "responses": {"200": {
        "content": {"application/json": {"schema": {"type": "object"}}}}}}}}}
    raw = httpx.Response(200, content=b'{}', headers={"content-type": "text/html"},
                         request=httpx.Request("GET", "https://example.test/api/v2/endpoint"))
    differences = response_differences(raw, contract)
    assert {item["path"] for item in differences} == {"$security", "$HTTP.Content-Type"}
