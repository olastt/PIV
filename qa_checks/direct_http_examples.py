"""Прямые httpx-запросы для примеров; не импортирует и не запускает автотесты."""

import json
import os
from pathlib import Path

import httpx
from dotenv import dotenv_values


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://petinvet.ru/api/v2"


def safe_fragment(path, body):
    if path == "/apiKey/byClinicCode" and isinstance(body, dict):
        copied = {key: value for key, value in body.items() if key in ("success", "message")}
        data = body.get("data")
        if isinstance(data, dict) and "apiKey" in data:
            copied["data"] = {"apiKey": "<API_KEY скрыт>"}
        return copied
    if path == "/discountCard" and isinstance(body, dict):
        data = body.get("data")
        if isinstance(data, dict):
            cards = []
            for card in data.get("card", [])[:1]:
                cards.append({"number": "<номер карты скрыт>" if isinstance(card.get("number"), str) else card.get("number"),
                              **{field: card.get(field) for field in ("is_default", "start_date", "end_date")}})
            return {"success": body.get("success"), "data": {"totalCount": data.get("totalCount"), "card": cards}}
    if path == "/medicalCards/vaccinations" and isinstance(body, dict):
        data = body.get("data", {})
        groups = []
        for group in data.get("vaccination", [])[:2]:
            if isinstance(group, list):
                groups.append([{"medcard_id": "<ID медкарты скрыт>"} for item in group[:1]])
            else:
                groups.append({"medcard_id": "<ID медкарты скрыт>"})
        return {"success": body.get("success"), "data": {"totalCount": data.get("totalCount"), "vaccination": groups}}
    if path == "/articles" and isinstance(body, dict):
        return {field: body.get(field) for field in ("current_page", "from", "to", "links", "next_page_url", "prev_page_url", "total")}
    return body


def main():
    config = {**dotenv_values(ROOT / ".env"), **os.environ}
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    setup = httpx.get(BASE + "/apiKey/byClinicCode", params={"code": config["CLINIC_CODE"]},
                     headers={**headers, "X-API-KEY": config["API_TOKEN_COLLECTION"]}, timeout=30)
    assert setup.status_code == 200, "Подготовленный ключ не позволяет получить ключ домена"
    key = setup.json()["data"]["apiKey"]
    cases = [
        ("api_key_without_auth", "GET", "/apiKey/byClinicCode", {"code": config["CLINIC_CODE"]}, None, None),
        ("missing_clinic_code", "GET", "/apiKey/byClinicCode", {}, None, config["API_TOKEN_COLLECTION"]),
        ("event_missing_device", "POST", "/event", None, {}, key),
        ("sms_missing_phone", "POST", "/sms/send", None, {}, key),
        ("discount_cards", "GET", "/discountCard", {"client_id": 1414}, None, key),
        ("vaccinations", "GET", "/medicalCards/vaccinations", {"client_id": 1414}, None, key),
        ("articles_size_10", "GET", "/articles", {"page": 1, "size": 10}, None, key),
        ("articles_size_1", "GET", "/articles", {"page": 1, "size": 1}, None, key),
        ("get_token_invalid_credentials", "POST", "/getToken", None,
         {"login": "qa_invalid_login", "password": "qa_invalid_password", "app_name": "piv"}, key),
    ]
    results = []
    print("Direct HTTP examples started; no pytest or project API clients used", flush=True)
    for name, method, path, params, payload, api_key in cases:
        request_headers = {**headers, **({"X-API-KEY": api_key} if api_key else {})}
        try:
            raw = httpx.request(method, BASE + path, params=params, json=payload, headers=request_headers, timeout=30)
            record = {"case": name, "method": method, "path": path,
                      "query": {field: "<CLINIC_CODE>" if field == "code" else value for field, value in (params or {}).items()},
                      "request_has_api_key": bool(api_key), "request_json": payload,
                      "status": raw.status_code, "content_type": raw.headers.get("content-type", "")}
            try:
                record["response_fragment"] = safe_fragment(path, raw.json())
            except ValueError:
                record["response_fragment"] = "Тело не является JSON; содержимое не сохранено"
            results.append(record)
        except httpx.RequestError as exc:
            results.append({"case": name, "method": method, "path": path, "exception": type(exc).__name__})
    output = {"base_url": BASE, "response_fragments_not_full_bodies": True, "results": results}
    (ROOT / "test-artifacts" / "direct-http-examples.json").write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(output, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
