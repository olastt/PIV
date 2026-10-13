"""Локальные проверки assertions: без HTTP, bootstrap и записи ключей в .env."""

from copy import deepcopy

import httpx
import pytest

from base.response import Response
from src.schemas.piv.errors import (
    PivErrorResponse,
    PivSmsCheckErrorResponse,
    PivValidation422Response,
    TokenUnauthorizedResponse,
)
from tests.helpers.piv_negative import assert_piv_error
from tests.helpers.piv_positive import (
    assert_articles_pagination,
    assert_collection_count,
    assert_json_body,
    assert_nonempty_string,
    assert_piv_success,
)


def response(body, status=200, path="/unknown"):
    return Response(httpx.Response(status, json=body, request=httpx.Request("GET", f"https://example.test{path}")))


@pytest.mark.parametrize("value", [False, None, "true", 1])
def test_http_200_with_unsuccessful_flag_is_rejected(value):
    with pytest.raises(AssertionError):
        assert_piv_success(response({"success": value}))


def test_successful_flag_is_accepted():
    assert assert_piv_success(response({"success": True}))["success"] is True


@pytest.mark.parametrize("value", ["", "  ", None, 123])
def test_empty_or_nonstring_key_is_rejected(value):
    with pytest.raises(AssertionError):
        assert_nonempty_string(value, "apiKey")


@pytest.mark.parametrize("content,media_type", [(b"not json", "application/json"), (b'{"success":true}', "text/html"), (b"", "application/json")])
def test_invalid_json_or_media_type_is_rejected(content, media_type):
    wrapped = Response(httpx.Response(200, content=content, headers={"content-type": media_type}))
    # Пустое тело не должно пройти схему/проверку success даже если парсер вернул {}.
    with pytest.raises(AssertionError):
        assert_piv_success(wrapped)


@pytest.mark.parametrize("media_type", ["application/json; charset=utf-8", "application/problem+json"])
def test_json_media_types_are_accepted(media_type):
    wrapped = Response(httpx.Response(200, json={"success": True}, headers={"content-type": media_type}))
    assert_json_body(wrapped)


@pytest.mark.parametrize("body,status,schema", [
    ({"success": False, "message": "Forbidden", "data": {"errorCode": 403}}, 403, PivErrorResponse),
    ({"success": False, "errorMessage": "Invalid code"}, 500, PivSmsCheckErrorResponse),
    ({"status": 401, "title": "Unauthorized", "detail": "Invalid credentials"}, 401, TokenUnauthorizedResponse),
])
@pytest.mark.parametrize("as_list", [False, True])
def test_error_object_and_single_item_list_are_accepted(body, status, schema, as_list):
    assert_piv_error(response([body] if as_list else body, status), status, schema)


@pytest.mark.parametrize("mutation", [{"success": True}, {"message": " "}, {"data": {"errorCode": "403"}}])
def test_semantically_invalid_error_is_rejected(mutation):
    body = {"success": False, "message": "Forbidden", "data": {"errorCode": 403}}
    body.update(mutation)
    with pytest.raises(AssertionError):
        assert_piv_error(response(body, 403), 403, PivErrorResponse)


@pytest.mark.parametrize("body", [[], [{}, {}]])
def test_empty_or_multiple_error_objects_are_rejected(body):
    with pytest.raises(AssertionError):
        assert_piv_error(response(body, 400), 400, PivErrorResponse)


@pytest.mark.parametrize("errors", [{}, {"page": []}, {"page": [" "]}, {"size": ["Required"]}])
def test_422_without_required_field_message_is_rejected(errors):
    with pytest.raises(AssertionError):
        assert_piv_error(response({"message": "Invalid input", "errors": errors}, 422), 422, PivValidation422Response, required_fields=("page",))


def test_422_with_required_field_message_is_accepted():
    assert_piv_error(response({"message": "Invalid input", "errors": {"page": ["Required"]}}, 422), 422, PivValidation422Response, required_fields=("page",))


def test_token_body_status_must_match_http_status():
    with pytest.raises(AssertionError):
        assert_piv_error(response({"status": 200, "title": "Unauthorized", "detail": "Invalid credentials"}, 401), 401, TokenUnauthorizedResponse)


@pytest.mark.parametrize("total,items", [(-1, []), (0, [{}]), (True, [])])
def test_impossible_collection_count_is_rejected(total, items):
    with pytest.raises(AssertionError):
        assert_collection_count({"totalCount": total, "items": items}, "items")


@pytest.mark.parametrize("total,items", [(0, []), (1, [{}]), (10, [{}])])
def test_collection_count_allows_empty_and_partial_results(total, items):
    assert_collection_count({"totalCount": total, "items": items}, "items")


PAGE = {"current_page": 1, "per_page": "1", "data": [{"id": 1}], "total": 2,
        "last_page": 2, "from": 1, "to": 1, "prev_page_url": None, "next_page_url": "https://example.test?page=2"}


@pytest.mark.parametrize("mutation", [
    {"current_page": 2}, {"per_page": "10"}, {"data": [{"id": 1}, {"id": 1}]},
    {"total": 0}, {"last_page": 0}, {"from": 0}, {"to": 2}, {"prev_page_url": "https://example.test?page=0"},
])
def test_inconsistent_pagination_is_rejected(mutation):
    body = deepcopy(PAGE)
    body.update(mutation)
    with pytest.raises(AssertionError):
        assert_articles_pagination(response(body), page=1, size=1)


def test_valid_pagination_is_accepted():
    assert_articles_pagination(response(PAGE), page=1, size=1)


def test_empty_page_after_last_is_accepted():
    body = deepcopy(PAGE)
    body.update(current_page=3, data=[], to=None, next_page_url=None)
    body["from"] = None
    assert_articles_pagination(response(body), page=3, size=1)


def test_registered_schema_still_rejects_wrong_field_type():
    wrapped = response({"success": True, "message": "OK", "data": {"client_id": "6"}}, path="/api/v2/clients/clientByPhone")
    with pytest.raises(AssertionError):
        wrapped.assert_status_code(200)


@pytest.mark.parametrize("as_list", [False, True])
def test_missing_parameter_message_supports_both_error_shapes(as_list):
    body = {"success": False, "message": "Missing phone", "data": {"errorCode": 400}}
    assert_piv_error(response([body] if as_list else body, 400), 400, PivErrorResponse, required_fields=("phone",))


def test_missing_parameter_message_must_identify_parameter():
    body = {"success": False, "message": "Unknown error", "data": {"errorCode": 400}}
    with pytest.raises(AssertionError):
        assert_piv_error(response(body, 400), 400, PivErrorResponse, required_fields=("phone",))


def test_duplicate_articles_within_page_size_are_rejected():
    body = deepcopy(PAGE)
    body.update(per_page="2", data=[{"id": 1}, {"id": 1}], to=2)
    with pytest.raises(AssertionError, match="повторяющиеся"):
        assert_articles_pagination(response(body), page=1, size=2)
