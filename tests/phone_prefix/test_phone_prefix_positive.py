import allure
import pytest
from Library.MakeyIS import Test


class TestPhonePrefixPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /getPhonePrefix")
    @allure.title("Получение префикса номера телефона")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_phone_prefix(self, phone_prefix_start):
        phone_prefix_start.get_phone_prefix()
