import allure
import pytest
from Library.MakeyIS import Test

from base.piv_client import PivApiClient
from src.config.url import Url
from src.schemas.piv.errors import PivErrorResponse
from tests.helpers.piv_negative import INVALID_API_KEY, assert_piv_error


class TestDiscountCardNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /discountCard")
    @allure.title("400 — отсутствует обязательный параметр client_id")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_missing_client_id_returns_400(self):
        response = PivApiClient().get(Url.GET_DISCOUNT_CARDS)
        assert_piv_error(response, 400, PivErrorResponse)
        assert "client_id" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /discountCard")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).get(
            Url.GET_DISCOUNT_CARDS,
            params={"client_id": 6},
        )
        assert_piv_error(response, 403, PivErrorResponse)
