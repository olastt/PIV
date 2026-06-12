from pydantic import TypeAdapter, ValidationError

INVALID_API_KEY = "00000000000000000000000000000000"


def unwrap_error_body(body):
    if isinstance(body, list):
        assert len(body) == 1, f"Expected single-item error list, got: {body}"
        body = body[0]
    return body


def assert_piv_error(response, status_code, schema):
    response.assert_status_code(status_code)
    body = unwrap_error_body(response.response_json)
    try:
        TypeAdapter(schema).validate_python(body)
    except ValidationError as exc:
        raise AssertionError(
            f"Response body does not match schema {schema}: {exc}\n"
            f"Response body: {body}"
        ) from exc
    return response
