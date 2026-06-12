import os

import allure
import pytest
from Library.MakeyIS import Test


class TestSmsPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("POST /sms/send")
    @allure.title("Отправка SMS")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_send_sms(self, sms_start):
        sms_start.send_sms(json_data={"phone": "79184140259"})

    # @pytest.mark.positive
    # @allure.epic("PIV")
    # @allure.feature("GET /sms/check")
    # @allure.title("Подтверждение номера по коду из SMS")
    # @Test(run_test=True, group_name="PIV", log=True)
    # @pytest.mark.skipif(
    #     not os.getenv("SMS_CODE"),
    #     reason="Нужен SMS_CODE в .env — код из SMS после send_sms",
    # )
    # def test_check_sms(self, sms_start):
    #     sms_start.check_sms()
