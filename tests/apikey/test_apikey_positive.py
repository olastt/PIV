import allure
import pytest
from Library.MakeyIS import Test


class TestApikeyPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /apiKey/byClinicCode")
    @allure.title("Получение apiKey клиники по коду")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_api_key_by_clinic_code(self, apikey_start):
        apikey_start.get_api_key_by_clinic_code()
