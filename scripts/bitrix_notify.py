#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from base.failure_report import FAILURES_FILE, format_bitrix_failure_block


def _parse_pytest_output(path: Path) -> tuple[str, str, str, str]:
    if not path.exists():
        return "0", "0", "0", ""

    text = path.read_text(encoding="utf-8", errors="replace")
    passed = str(sum(int(x) for x in re.findall(r"(\d+) passed", text)))
    failed = str(sum(int(x) for x in re.findall(r"(\d+) failed", text)))
    error = str(sum(int(x) for x in re.findall(r"(\d+) error", text)))
    failed_tests = "|".join(
        line.replace("FAILED ", "", 1).split(" - ", 1)[0]
        for line in text.splitlines()
        if line.startswith("FAILED ")
    )
    return passed, failed, error, failed_tests


def _load_failures(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


def _build_message(
    platform_label: str,
    report_url: str,
    passed: str,
    failed: str,
    error: str,
    failed_tests: str,
    failures: list[dict],
) -> str:
    message = (
        f"🚀 {platform_label} - Автотесты API прогнаны!\n\n"
        f"✅ Passed: {passed}\n"
        f"❌ Failed: {failed}\n"
        f"⚠️ Errors: {error}\n"
    )

    if failures:
        message += "\nУпавшие тесты с данными запроса:\n"
        for record in failures[:5]:
            message += format_bitrix_failure_block(record) + "\n\n"
        if len(failures) > 5:
            message += f"... и ещё {len(failures) - 5} упавших тестов\n"
    elif failed_tests.strip():
        failed_list = "\n".join(item for item in failed_tests.split("|") if item.strip())
        message += f"\nУпавшие тесты:\n{failed_list}\n"

    message += f"\n📊 Отчёт: {report_url}"
    return message


def main() -> int:
    parser = argparse.ArgumentParser(description="Send PIV autotest results to Bitrix24")
    parser.add_argument("--platform-label", default="PIV")
    parser.add_argument("--report-url", required=True)
    parser.add_argument("--failures-file", default=str(FAILURES_FILE))
    parser.add_argument("--pytest-output", default="pytest-output.txt")
    args = parser.parse_args()

    webhook = os.environ.get("BITRIX_WEBHOOK_URL", "").rstrip("/")
    chat_id = os.environ.get("BITRIX_CHAT_ID", "")
    if not webhook or not chat_id:
        print("BITRIX_WEBHOOK_URL and BITRIX_CHAT_ID are required", file=sys.stderr)
        return 1

    passed = os.environ.get("PASSED")
    failed = os.environ.get("FAILED")
    error = os.environ.get("ERROR")
    failed_tests = os.environ.get("FAILED_TESTS", "")

    if passed is None or failed is None or error is None:
        passed, failed, error, parsed_failed_tests = _parse_pytest_output(Path(args.pytest_output))
        if not failed_tests:
            failed_tests = parsed_failed_tests

    failures = _load_failures(Path(args.failures_file))
    message = _build_message(
        args.platform_label,
        args.report_url,
        passed,
        failed,
        error,
        failed_tests,
        failures,
    )

    data = urllib.parse.urlencode({"DIALOG_ID": chat_id, "MESSAGE": message}).encode("utf-8")
    request = urllib.request.Request(f"{webhook}/im.message.add.json", data=data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
