import os

import allure

from base.methods.sms.sms_methods import SmsMethods


class SmsStart:
    def __init__(self):
        self.sms = SmsMethods()

    def send_sms(self, phone=None, json_data=None):
        phone = phone or os.getenv("CLIENT_PHONE", "79184140259")
        json_data = json_data or {"phone": phone}
        with allure.step("POST /sms/send"):
            response = self.sms.send_sms(json_data)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    # def check_sms(self, phone=None, code=None):
    #     phone = phone or os.getenv("CLIENT_PHONE", "79184140259")
    #     code = code or os.getenv("SMS_CODE")
    #     if not code:
    #         raise AssertionError(
    #             "Для проверки SMS задайте SMS_CODE в .env (код из реального сообщения после send_sms)"
    #         )
    #     with allure.step("GET /sms/check"):
    #         response = self.sms.check_sms(phone, code)
    #     with allure.step("Проверка статус кода 200"):
    #         response.assert_status_code(200)
    #     return response
