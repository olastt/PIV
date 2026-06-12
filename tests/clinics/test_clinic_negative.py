import allure
import pytest
from Library.MakeyIS import Test

from base.piv_client import PivApiClient
from src.config.url import Url
from src.schemas.piv.errors import PivErrorResponse
from tests.helpers.piv_negative import INVALID_API_KEY, assert_piv_error


class TestClinicNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /clinics")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).get(Url.GET_CLINICS)
        assert_piv_error(response, 403, PivErrorResponse)
