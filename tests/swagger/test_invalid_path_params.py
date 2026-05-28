import allure
import pytest

from base.main_request_class import ApiClient
from tests.swagger.data import (
    INVALID_PATH_EXCLUDED_CASES,
    INVALID_PATH_CAN_RETURN_OK,
    NEGATIVE_STATUS_CODES,
    SWAGGER_ENDPOINTS,
    _invalid_path_title,
    _resolve_path,
    _send,
)


@pytest.mark.negative
@allure.epic("Swagger negative coverage")
@pytest.mark.parametrize(
    ("method", "path"),
    [
        (method, path)
        for method, path in SWAGGER_ENDPOINTS
        if "{" in path and (method, path) not in INVALID_PATH_EXCLUDED_CASES
    ],
    ids=[
        _invalid_path_title(method, path)
        for method, path in SWAGGER_ENDPOINTS
        if "{" in path and (method, path) not in INVALID_PATH_EXCLUDED_CASES
    ],
)
def test_swagger_endpoints_reject_invalid_path_parameters(method, path):
    allure.dynamic.title(_invalid_path_title(method, path))
    client = ApiClient()

    response = _send(client, method, _resolve_path(path, invalid_params=True))

    expected_status_codes = NEGATIVE_STATUS_CODES.copy()
    if (method, path) in INVALID_PATH_CAN_RETURN_OK:
        expected_status_codes.append(200)
    response.assert_status_code(expected_status_codes)
