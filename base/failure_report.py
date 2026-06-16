import json
from pathlib import Path

import allure

from base.request_context import HttpExchange, get_all_exchanges, get_last_exchange

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FAILURES_DIR = PROJECT_ROOT / "test-artifacts"
FAILURES_FILE = FAILURES_DIR / "failures.json"
BITRIX_BODY_LIMIT = 800
BITRIX_ERROR_LIMIT = 400


def init_failures_file() -> None:
    FAILURES_DIR.mkdir(parents=True, exist_ok=True)
    FAILURES_FILE.write_text("[]", encoding="utf-8")


def _truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return f"{text[:limit]}\n... (обрезано, всего {len(text)} символов)"


def format_failure_summary(test_nodeid: str, error_message: str, exchange: HttpExchange | None) -> str:
    lines = [
        f"Тест: {test_nodeid}",
        f"Ошибка: {error_message}",
    ]
    if exchange:
        lines.extend(
            [
                "",
                f"HTTP: {exchange.method} {exchange.url}",
                f"Статус: {exchange.status_code}",
                "",
                "cURL:",
                exchange.curl,
                "",
                "Тело ответа:",
                exchange.response_body or "(пусто)",
            ]
        )
    else:
        lines.append("")
        lines.append("HTTP-запрос для этого теста не зафиксирован.")
    return "\n".join(lines)


def append_failure_record(test_nodeid: str, error_message: str, exchange: HttpExchange | None) -> dict:
    record = {
        "test": test_nodeid,
        "error": error_message,
        "method": exchange.method if exchange else None,
        "url": exchange.url if exchange else None,
        "status_code": exchange.status_code if exchange else None,
        "request_body": exchange.request_body if exchange else None,
        "curl": exchange.curl if exchange else None,
        "response_body": exchange.response_body if exchange else None,
    }

    failures = []
    if FAILURES_FILE.exists():
        try:
            failures = json.loads(FAILURES_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            failures = []

    failures.append(record)
    FAILURES_FILE.write_text(
        json.dumps(failures, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return record


def report_test_failure(test_nodeid: str, error_message: str) -> None:
    exchange = get_last_exchange()
    summary = format_failure_summary(test_nodeid, error_message, exchange)

    allure.attach(
        summary,
        name="Данные упавшего теста",
        attachment_type=allure.attachment_type.TEXT,
    )

    for index, item in enumerate(get_all_exchanges(), start=1):
        suffix = f" #{index}" if len(get_all_exchanges()) > 1 else ""
        allure.attach(
            item.curl,
            name=f"cURL упавшего запроса{suffix}",
            attachment_type=allure.attachment_type.TEXT,
        )
        if item.response_body:
            allure.attach(
                item.response_body,
                name=f"Ответ упавшего запроса{suffix}",
                attachment_type=allure.attachment_type.JSON
                if item.response_body.lstrip().startswith(("{", "["))
                else allure.attachment_type.TEXT,
            )

    append_failure_record(test_nodeid, error_message, exchange)


def format_bitrix_failure_block(record: dict) -> str:
    lines = [f"• {record['test']}"]
    if record.get("error"):
        lines.append(f"  Ошибка: {_truncate(record['error'], BITRIX_ERROR_LIMIT)}")
    if record.get("url"):
        lines.append(f"  HTTP: {record.get('method')} {record['url']} → {record.get('status_code')}")
    if record.get("curl"):
        lines.append(f"  cURL: {_truncate(record['curl'], BITRIX_BODY_LIMIT)}")
    if record.get("response_body"):
        lines.append(f"  Ответ: {_truncate(record['response_body'], BITRIX_BODY_LIMIT)}")
    return "\n".join(lines)
