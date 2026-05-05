import json
import shlex

import allure


def _request_to_curl(request) -> str:
    """
    Собирает cURL из httpx.Request с безопасным quoting заголовков и тела.

    curlify2 даёт -H "sec-ch-ua: "Chromium";v="120"..." — внутренние кавычки
    ломают строку в shell и при импорте в Postman; shlex.quote оборачивает
    каждый заголовок в одинарные кавычки по правилам POSIX.
    """
    parts = ["curl", "-X", shlex.quote(request.method.upper())]

    skip_headers = {"content-length"}
    for name, value in request.headers.items():
        if name.lower() in skip_headers:
            continue
        parts.extend(["-H", shlex.quote(f"{name}: {value}")])

    if request.content:
        body = request.content.decode("utf-8", errors="replace")
        parts.extend(["--data-binary", shlex.quote(body)])

    parts.append(shlex.quote(str(request.url)))
    return " ".join(parts)


def attach_response_info(response):
    allure.attach(_request_to_curl(response.request), name="cURL команда", attachment_type=allure.attachment_type.TEXT)

    if response.text:
        try:
            response_json = response.json()
            readable_json = json.dumps(response_json, indent=2, ensure_ascii=False)
            allure.attach(readable_json, name="Тело ответа", attachment_type=allure.attachment_type.JSON)
        except ValueError:
            allure.attach(response.text, name="Тело ответа", attachment_type=allure.attachment_type.TEXT)
