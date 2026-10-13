import httpx
import pytest

from base.response import Response
from tests.helpers.access import assert_access_denied


def response(body, status):
    return Response(httpx.Response(status, json=body))


@pytest.mark.parametrize("status", [401, 403])
@pytest.mark.parametrize("as_list", [False, True])
def test_denied_error_is_accepted(status, as_list):
    body = {"success": False, "message": "Access denied", "data": {"errorCode": status}}
    assert_access_denied(response([body] if as_list else body, status))


@pytest.mark.parametrize("body,status", [
    ({"message": "OK"}, 200),
    ({"message": "Server failed"}, 500),
    ({"success": True, "message": "Denied"}, 403),
    ({"message": "Denied", "data": {"apiKey": "synthetic-secret"}}, 403),
    ({"message": "Denied", "data": {"client_id": 123}}, 403),
    ({"message": "Denied", "client_id": 123}, 403),
    ({"message": "Denied", "data": [{"id": 123}]}, 403),
    ({"message": " "}, 403),
])
def test_success_server_error_and_data_leak_are_rejected(body, status):
    with pytest.raises(AssertionError):
        assert_access_denied(response(body, status))


def test_not_found_is_only_accepted_when_requested():
    wrapped = response({"success": False, "message": "Client not found"}, 404)
    with pytest.raises(AssertionError):
        assert_access_denied(wrapped)
    assert_access_denied(wrapped, statuses=(401, 403, 404))
