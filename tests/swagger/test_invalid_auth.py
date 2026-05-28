import allure
import pytest

from base.main_request_class import ApiClient
from tests.swagger.data import (
    INVALID_AUTH_STATUS_CODES,
    SWAGGER_ENDPOINTS,
    _invalid_auth_title,
    _resolve_path,
    _send,
)


@pytest.mark.negative
@allure.epic("Swagger negative coverage")
@pytest.mark.parametrize(
    ("method", "path"),
    SWAGGER_ENDPOINTS,
    ids=[_invalid_auth_title(method, path) for method, path in SWAGGER_ENDPOINTS],
)
def test_swagger_endpoints_reject_invalid_authorization(method, path):
    allure.dynamic.title(_invalid_auth_title(method, path))
    client = ApiClient(api_key="pytest-invalid-token")
    headers = {"X-TOKEN": "pytest-invalid-token"}

    response = _send(client, method, _resolve_path(path), headers=headers, invalid_query=False)

    response.assert_status_code(INVALID_AUTH_STATUS_CODES)
