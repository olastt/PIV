"""Проверка отказа в доступе без предположения об одном точном статусе."""

from tests.helpers.piv_negative import unwrap_error_body
from tests.helpers.piv_positive import assert_json_body, assert_nonempty_string


def assert_access_denied(response, statuses=(401, 403)):
    response.assert_status_code(list(statuses))
    body = unwrap_error_body(assert_json_body(response))
    assert isinstance(body, dict), "Ошибка доступа должна быть объектом"
    assert set(body) <= {"success", "message", "data", "status", "title", "detail"}, "Ответ ошибки содержит неожиданные поля"
    if "success" in body:
        assert body["success"] is False, "Отказ в доступе не может быть успешным"
    message = body.get("message") or body.get("detail")
    assert_nonempty_string(message, "Сообщение отказа")
    data = body.get("data")
    assert data is None or (isinstance(data, dict) and set(data) <= {"errorCode"}), "При отказе в доступе возвращены данные"
    if "status" in body:
        assert body["status"] == response.response_status, "status не совпадает с HTTP"
    return body
