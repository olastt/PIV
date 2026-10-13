import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_piv_success


class TestPhonePrefixPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /getPhonePrefix")
    @allure.title("Получение префикса номера телефона")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_phone_prefix(self, phone_prefix_start):
        body = assert_piv_success(phone_prefix_start.get_phone_prefix())
        assert body["data"]["prefix"] > 0, "Телефонный префикс должен быть положительным"
