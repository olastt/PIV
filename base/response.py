from json import JSONDecodeError


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
        return self

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json} \n" \
            f"Response headers: {self.response_headers}"
