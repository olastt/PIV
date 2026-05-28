from json import JSONDecodeError

from pydantic import TypeAdapter, ValidationError


class Response:
    STATUS_CODE_ERROR = "Статус-код ожидался: {}, получен: {}"

    def __init__(self, response, json=True, text=False):
        self.response = response
        self.response_status = response.status_code
        self.response_headers = response.headers

        self.response_text = ''
        self.response_json = {}

        if text:
            try:
                self.response_text = response.text
            except UnicodeDecodeError:
                self.response_text = None

        if json:
            try:
                self.response_json = response.json() if response.content else {}
            except (JSONDecodeError, UnicodeDecodeError):
                self.response_json = None

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, \
                self.STATUS_CODE_ERROR.format(", ".join(map(str, status_code)), self.response_status)
        else:
            assert self.response_status == status_code, \
                self.STATUS_CODE_ERROR.format(status_code, self.response_status)
        if 200 <= self.response_status < 300:
            self.assert_registered_schema()
        return self

    def assert_schema(self, schema):
        try:
            TypeAdapter(schema).validate_python(self.response_json)
        except ValidationError as exc:
            raise AssertionError(
                f"Response body does not match schema {schema}: {exc}\n"
                f"Response body: {self.response_json}"
            ) from exc
        return self

    def assert_registered_schema(self):
        from src.schemas.response_registry import schema_for_response

        schema = schema_for_response(self.response)
        if schema is not None:
            self.assert_schema(schema)
        return self

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json} \n" \
            f"Response headers: {self.response_headers}"
