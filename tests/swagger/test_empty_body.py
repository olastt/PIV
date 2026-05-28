import allure
import pytest

from base.main_request_class import ApiClient
from tests.swagger.data import (
    DELETE_NOT_FOUND_CASES,
    MUTATING_METHODS,
    NEGATIVE_STATUS_CODES,
    SWAGGER_ENDPOINTS,
    _empty_body_title,
    _resolve_path,
    _send,
)


@pytest.mark.negative
@allure.epic("Swagger negative coverage")
@pytest.mark.parametrize(
    ("method", "path"),
    [(method, path) for method, path in SWAGGER_ENDPOINTS if method in MUTATING_METHODS],
    ids=[_empty_body_title(method, path) for method, path in SWAGGER_ENDPOINTS if method in MUTATING_METHODS],
)
def test_swagger_mutating_endpoints_reject_empty_body(method, path):
    allure.dynamic.title(_empty_body_title(method, path))
    client = ApiClient()

    response = _send(client, method, _resolve_path(path), json_data={})

    response.assert_status_code(NEGATIVE_STATUS_CODES)


@pytest.mark.negative
@allure.epic("Swagger negative coverage")
@pytest.mark.parametrize(
    ("method", "path", "path_overrides", "expected_status", "case_title"),
    DELETE_NOT_FOUND_CASES,
    ids=[case_title for _, _, _, _, case_title in DELETE_NOT_FOUND_CASES],
)
def test_swagger_delete_endpoints_return_not_found_for_missing_numeric_id(
    method,
    path,
    path_overrides,
    expected_status,
    case_title,
):
    allure.dynamic.title(f"{case_title}: {method} {path}")
    client = ApiClient()

    response = _send(client, method, _resolve_path(path, overrides=path_overrides))

    response.assert_status_code(expected_status)
