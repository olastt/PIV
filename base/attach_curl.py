import json
import shlex

import allure

from base.request_context import record_exchange


def _request_body(request) -> str:
    if not request.content:
        return ""
    return request.content.decode("utf-8", errors="replace")


def _response_body(response) -> str:
    if not response.text:
        return ""
    try:
        return json.dumps(response.json(), indent=2, ensure_ascii=False)
    except ValueError:
        return response.text


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
    curl_command = _request_to_curl(response.request)
    body = _response_body(response)

    allure.attach(curl_command, name="cURL команда", attachment_type=allure.attachment_type.TEXT)

    if body:
        attachment_type = (
            allure.attachment_type.JSON
            if body.lstrip().startswith(("{", "["))
            else allure.attachment_type.TEXT
        )
        allure.attach(body, name="Тело ответа", attachment_type=attachment_type)

    record_exchange(
        method=response.request.method.upper(),
        url=str(response.url),
        status_code=response.status_code,
        request_body=_request_body(response.request),
        response_body=body,
        curl=curl_command,
    )
