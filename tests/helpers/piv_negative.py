from pydantic import TypeAdapter, ValidationError

from tests.helpers.piv_positive import assert_json_body, assert_nonempty_string

INVALID_API_KEY = "00000000000000000000000000000000"


def unwrap_error_body(body):
    if isinstance(body, list):
        assert len(body) == 1, f"Expected single-item error list, got: {body}"
        body = body[0]
    return body


def assert_piv_error(response, status_code, schema, required_fields=()):
    response.assert_status_code(status_code)
    body = unwrap_error_body(assert_json_body(response))
    try:
        TypeAdapter(schema).validate_python(body)
    except ValidationError as exc:
        raise AssertionError(
            f"Response body does not match schema {schema}: {exc}\n"
            f"Response body: {body}"
        ) from exc
    if "success" in body:
        assert body["success"] is False, "Ответ ошибки должен содержать success=false"
    for field in ("message", "errorMessage", "title", "detail"):
        if field in body:
            assert_nonempty_string(body[field], field)
    if "status" in body:
        assert body["status"] == status_code, "status в теле не совпадает с HTTP-статусом"
    if "errors" in body:
        assert body["errors"], "422 должен содержать ошибки валидации"
        for field, messages in body["errors"].items():
            assert_nonempty_string(field, "errors key")
            assert messages, "Для поля должна быть хотя бы одна ошибка"
            for message in messages:
                assert_nonempty_string(message, "validation message")
        assert set(required_fields) <= body["errors"].keys(), "Нет ошибок обязательных полей"
    elif required_fields:
        for field in required_fields:
            assert field.lower() in body["message"].lower(), f"Сообщение ошибки должно указывать поле {field}"
    return response
