import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_nonempty_string, assert_piv_success


class TestApikeyPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /apiKey/byClinicCode")
    @allure.title("Получение apiKey клиники по коду")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_api_key_by_clinic_code(self, apikey_start):
        body = assert_piv_success(apikey_start.get_api_key_by_clinic_code())
        assert_nonempty_string(body["data"]["apiKey"], "data.apiKey")
