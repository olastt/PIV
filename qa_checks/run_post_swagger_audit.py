"""Разрешённый пользователем POST-аудит: без .env/сырых ответов/секретов."""

import argparse
import hashlib
import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

from qa_checks.swagger_contract import json_type, read_contract, response_differences
from src.config.url import Url


ROOT = Path(__file__).resolve().parents[1]


def main(swagger, qa_data):
    env_file = ROOT / ".env"
    before = hashlib.sha256(env_file.read_bytes()).digest()
    load_dotenv(env_file)
    contract = read_contract(swagger)
    data = json.loads(Path(qa_data).read_text(encoding="utf-8"))
    phone = data["primary_client"]["phone"]
    assert isinstance(phone, str) and phone.isdigit() and len(phone) == 10, "Нужен тестовый телефон без ведущей 7"
    sms_phone = int("7" + phone)
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    setup = httpx.get(Url.DOMAIN_PET_PROD + Url.GET_API_KEY_BY_CLINIC_CODE,
                     headers={**headers, "X-API-KEY": os.environ["API_TOKEN_COLLECTION"]},
                     params={"code": os.environ["CLINIC_CODE"]}, timeout=30)
    assert setup.status_code == 200, "Не удалось получить ключ домена через GET"
    key = setup.json()["data"]["apiKey"]
    assert isinstance(key, str) and key, "Ключ домена отсутствует"
    login = os.getenv("LOGIN_PIV") or os.getenv("LOGIN")
    password = os.getenv("PASSWORD_PIV") or os.getenv("PASSWORD")
    app_name = os.getenv("APP_NAME_PIV") or os.getenv("APP_NAME")
    assert login and password and app_name, "Нужны подготовленные credentials ВМ"
    auth = {"login": login, "password": password, "app_name": app_name}
    event = {"device_id": 1, "title": "QA Swagger contract audit"}
    cases = [
        ("event_missing_device_id", "/event", {}, key),
        ("event_missing_title", "/event", {"device_id": 1}, key),
        ("event_invalid_api_key", "/event", event, "00000000000000000000000000000000"),
        ("event_valid", "/event", event, key),
        ("sms_missing_phone", "/sms/send", {}, key),
        ("sms_invalid_api_key", "/sms/send", {"phone": sms_phone}, "00000000000000000000000000000000"),
        ("sms_valid", "/sms/send", {"phone": sms_phone}, key),
        ("token_valid_json", "/getToken", auth, key),
        ("token_missing_app_name", "/getToken", {"login": login, "password": password}, key),
    ]
    results = []
    print("POST audit started; credentials and response bodies are not saved", flush=True)
    for name, path, body, api_key in cases:
        try:
            raw = httpx.post(Url.DOMAIN_PET_PROD + path, headers={**headers, "X-API-KEY": api_key}, json=body, timeout=30)
            record = {"case": name, "method": "POST", "path": path,
                      "status": raw.status_code, "content_type": raw.headers.get("content-type", ""),
                      "request_field_types": {field: json_type(value) for field, value in body.items()},
                      "differences": response_differences(raw, contract)}
            try:
                parsed = raw.json()
                record["body_type"] = json_type(parsed)
                if isinstance(parsed, list):
                    record["error_list_length"] = len(parsed)
                if isinstance(parsed, dict) and isinstance(parsed.get("success"), bool):
                    record["success"] = parsed["success"]
            except ValueError:
                record["body_type"] = "not JSON"
            results.append(record)
        except httpx.RequestError as exc:
            results.append({"case": name, "method": "POST", "path": path, "exception": type(exc).__name__})
    unchanged = before == hashlib.sha256(env_file.read_bytes()).digest()
    output = {"env_unchanged": unchanged, "results": results}
    (ROOT / "test-artifacts" / "readonly-post-swagger-audit-results.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(output, ensure_ascii=True, indent=2))
    assert unchanged, ".env изменился"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--swagger", required=True)
    parser.add_argument("--qa-data", required=True)
    args = parser.parse_args()
    main(args.swagger, args.qa_data)
