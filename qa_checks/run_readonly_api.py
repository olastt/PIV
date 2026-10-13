"""GET-прогон: clinic key через GET, без POST/записи .env/сырых артефактов.

Запуск: python -m qa_checks.run_readonly_api
"""

import contextlib
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlsplit

import httpx
import pytest

import tests.conftest as api_fixtures
from base.piv_client import PivApiClient
from src.config.url import Url
from tests.helpers.piv_positive import assert_nonempty_string, assert_piv_success


ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    "tests/apikey/test_apikey_negative.py", "tests/articles", "tests/clients",
    "tests/clinics", "tests/discount_card", "tests/domain_name", "tests/medicalcards",
    "tests/phone_prefix", "tests/piv_admissions",
    "tests/security", "tests/data_cases",
]


class SafeResults:
    def __init__(self, contract=None):
        self.results = []
        self.exchange = None
        self.contract = contract
        self.contract_findings = []

    def capture_exchange(self, raw):
        self.exchange = {
            "method": raw.request.method,
            "path": urlsplit(str(raw.url)).path,
            "status": raw.status_code,
            "content_type": raw.headers.get("content-type", ""),
        }
        if self.contract:
            from qa_checks.swagger_contract import response_differences
            differences = response_differences(raw, self.contract)
            if differences:
                self.contract_findings.append({**self.exchange, "differences": differences})
        if self.contract and self.exchange["path"].endswith("/clinics") and raw.status_code == 200:
            body = raw.json()
            data = body.get("data") if isinstance(body, dict) else None
            self.exchange["data_keys"] = sorted(data) if isinstance(data, dict) else []
        if self.exchange["path"].endswith("/discountCard"):
            try:
                body = raw.json()
            except ValueError:
                return
            data = body.get("data") if isinstance(body, dict) else None
            groups = data if isinstance(data, list) else [data] if isinstance(data, dict) else []
            cards = [card for group in groups if isinstance(group, dict)
                     for card in group.get("card", []) if isinstance(card, dict)]
            self.exchange["card_count"] = len(cards)
            if cards:
                first = cards[0]
                self.exchange["card_field_types"] = {
                    field: type(first[field]).__name__ if field in first else "missing"
                    for field in ("number", "is_default", "start_date", "end_date")
                }
                self.exchange["number_is_digit_string"] = isinstance(first.get("number"), str) and first["number"].isdigit()
                flag = first.get("is_default")
                self.exchange["default_flag_is_zero_or_one"] = type(flag) is int and flag in (0, 1)
        if self.exchange["path"].endswith("/apiKey/byClinicCode"):
            try:
                body = raw.json()
            except ValueError:
                return
            if isinstance(body, dict):
                data = body.get("data")
                key = data.get("apiKey") if isinstance(data, dict) else None
                self.exchange["nonempty_api_key"] = isinstance(key, str) and bool(key.strip())
                self.exchange["success_true"] = body.get("success") is True
                self.exchange["request_has_api_key"] = "X-API-KEY" in raw.request.headers

    def pytest_runtest_setup(self, item):
        self.exchange = None

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        report = outcome.get_result()
        if report.when == "call" or report.failed or report.skipped:
            record = {"test": item.nodeid, "phase": report.when, "outcome": report.outcome}
            if self.exchange:
                record["http"] = self.exchange
            if call.excinfo:
                exc = call.excinfo.value
                record["exception"] = type(exc).__name__
                # Не сохраняем тела/inputs Pydantic или значения credentials.
                cause = exc.__cause__
                if hasattr(cause, "errors"):
                    record["schema_errors"] = [
                        {"location": list(error["loc"]), "type": error["type"]}
                        for error in cause.errors()
                    ]
                elif isinstance(exc, AssertionError):
                    record["assertion"] = str(exc).splitlines()[0]
            self.results.append(record)


def forbidden(*args, **kwargs):
    raise RuntimeError("Read-only runner blocked POST or credential persistence")


def main(priority=False, case=None, qa_data=None, swagger=None):
    env_file = ROOT / ".env"
    before = hashlib.sha256(env_file.read_bytes()).digest()
    if swagger:
        from qa_checks.swagger_contract import read_contract
        contract = read_contract(swagger)
    else:
        contract = None
    results = SafeResults(contract)
    original_get = httpx.get
    original_client_init = PivApiClient.__init__
    clinic_key = {}

    def get_with_timeout(*args, **kwargs):
        kwargs["timeout"] = 15
        return original_get(*args, **kwargs)

    def client_init(client, *args, **kwargs):
        kwargs["base_url"] = Url.DOMAIN_PET_PROD
        if kwargs.get("api_key") is None and clinic_key:
            kwargs["api_key"] = clinic_key["value"]
        original_client_init(client, *args, **kwargs)

    def existing_session(*args, **kwargs):
        assert os.getenv("API_TOKEN_COLLECTION"), "Для apiKey negative нужен существующий API_TOKEN_COLLECTION"
        raw = PivApiClient(api_key=os.getenv("API_TOKEN_COLLECTION")).get(
            Url.GET_API_KEY_BY_CLINIC_CODE, params={"code": os.getenv("CLINIC_CODE", "10001")}
        )
        raw.assert_status_code(200)
        body = assert_piv_success(raw)
        assert_nonempty_string(body["data"]["apiKey"], "data.apiKey")
        clinic_key["value"] = body["data"]["apiKey"]

    print("GET-only API run started; raw output and credential persistence disabled", flush=True)
    with contextlib.ExitStack() as stack:
        stack.enter_context(patch("base.methods.token.token_start.TokenStart.bootstrap_piv_session", existing_session))
        stack.enter_context(patch("base.methods.token.token_start.write_collection_key_to_env", forbidden))
        stack.enter_context(patch("base.methods.token.token_start.write_clinic_api_key_to_env", forbidden))
        stack.enter_context(patch("base.methods.token.token_start.set_key", forbidden))
        stack.enter_context(patch.object(api_fixtures, "init_failures_file", lambda: None))
        stack.enter_context(patch.object(api_fixtures, "report_test_failure", lambda *args: None))
        stack.enter_context(patch("base.main_request_class.attach_response_info", results.capture_exchange))
        stack.enter_context(patch.object(PivApiClient, "__init__", client_init))
        stack.enter_context(patch.object(httpx, "get", get_with_timeout))
        stack.enter_context(patch.object(httpx, "post", forbidden))
        stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
        stack.enter_context(contextlib.redirect_stderr(io.StringIO()))
        targets = ["tests/security", "tests/data_cases", "tests/clients/test_clients_positive.py"] if priority else TARGETS
        if case == "apikey":
            targets = ["tests/security/test_missing_api_key.py::test_missing_api_key_denies_access[/apiKey/byClinicCode-code]"]
        elif case == "client-data":
            targets = ["tests/data_cases"]
        elif case == "discount-switch":
            targets = ["tests/data_cases/test_populated_client.py::test_switch_populated_empty_populated_client[/discountCard-card]"]
        elif case == "swagger-audit":
            assert contract, "Нужен путь --swagger"
            targets = TARGETS
        elif case == "swagger-details":
            assert contract, "Нужен путь --swagger"
            targets = ["tests/clinics/test_clinic_positive.py", "tests/data_cases/test_populated_client.py::test_switch_populated_empty_populated_client[/medicalCards/vaccinations-vaccination]"]
        if qa_data:
            assert case != "apikey", "Данные клиентов не нужны в диагностике apiKey"
            targets = targets + ["--qa-client-data", qa_data]
        code = pytest.main(targets + ["-q", "-o", "addopts=", "--tb=no", "--show-capture=no"], plugins=[results])

    unchanged = before == hashlib.sha256(env_file.read_bytes()).digest()
    output = {"exit_code": int(code), "env_unchanged": unchanged, "results": results.results}
    if contract:
        output["contract_findings"] = results.contract_findings
    # Только технические метаданные, без сырых запросов/ответов и персональных данных.
    (ROOT / "test-artifacts").mkdir(exist_ok=True)
    filename = "readonly-priority-results.json" if priority else "readonly-results.json"
    if case:
        filename = {
            "apikey": "readonly-apikey-access-results.json",
            "client-data": "readonly-client-data-results.json",
            "discount-switch": "readonly-discount-switch-results.json",
            "swagger-audit": "readonly-swagger-audit-results.json",
            "swagger-details": "readonly-swagger-details-results.json",
        }[case]
    (ROOT / "test-artifacts" / filename).write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    if case == "swagger-audit":
        from collections import Counter
        display = {"exit_code": int(code), "env_unchanged": unchanged,
                   "outcomes": dict(Counter(item["outcome"] for item in results.results)),
                   "contract_findings": results.contract_findings}
    else:
        display = output
    print(json.dumps(display, ensure_ascii=True, indent=2))
    assert unchanged, ".env изменился во время read-only прогона"
    return int(code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--priority", action="store_true", help="Только новые приоритетные сценарии и client lookup")
    parser.add_argument("--case", choices=["apikey", "client-data", "discount-switch", "swagger-audit", "swagger-details"], help="Отдельная группа GET-проверок")
    parser.add_argument("--qa-data", help="JSON с подготовленными тестовыми клиентами")
    parser.add_argument("--swagger", help="Предоставленный OpenAPI YAML")
    args = parser.parse_args()
    raise SystemExit(main(priority=args.priority, case=args.case, qa_data=args.qa_data, swagger=args.swagger))
