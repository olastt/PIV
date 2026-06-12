import allure
import pytest
from Library.MakeyIS import Test

from base.methods.apikey.apikey_methods import ApikeyMethods
from src.config.url import Url
from src.schemas.piv.errors import PivErrorResponse
from tests.helpers.piv_negative import assert_piv_error


class TestApikeyNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /apiKey/byClinicCode")
    @allure.title("400 — отсутствует обязательный параметр code")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_missing_code_returns_400(self):
        response = ApikeyMethods().get(Url.GET_API_KEY_BY_CLINIC_CODE)
        assert_piv_error(response, 400, PivErrorResponse)
        assert "code" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /apiKey/byClinicCode")
    @allure.title("404 — несуществующий код клиники")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_invalid_clinic_code_returns_404(self):
        response = ApikeyMethods().get(
            Url.GET_API_KEY_BY_CLINIC_CODE,
            params={"code": "99999999"},
        )
        assert_piv_error(response, 404, PivErrorResponse)
