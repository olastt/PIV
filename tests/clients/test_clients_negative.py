import allure
import pytest
from Library.MakeyIS import Test

from base.piv_client import PivApiClient
from src.config.url import Url
from src.schemas.piv.errors import PivErrorResponse
from tests.helpers.piv_negative import INVALID_API_KEY, assert_piv_error


class TestClientsNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /clients/clientByPhone")
    @allure.title("400 — отсутствует обязательный параметр phone")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_missing_phone_returns_400(self):
        response = PivApiClient().get(Url.GET_CLIENT_BY_PHONE)
        assert_piv_error(response, 400, PivErrorResponse)
        assert "phone" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /clients/clientByPhone")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).get(
            Url.GET_CLIENT_BY_PHONE,
            params={"phone": "9184140259"},
        )
        assert_piv_error(response, 403, PivErrorResponse)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /clients/clientByPhone")
    @allure.title("404 — клиент с таким номером не найден")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_phone_not_found_returns_404(self):
        response = PivApiClient().get(
            Url.GET_CLIENT_BY_PHONE,
            params={"phone": "0000000000"},
        )
        assert_piv_error(response, 404, PivErrorResponse)
