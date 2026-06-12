import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class SmsMethods(PivApiClient):
    @allure.step("POST /sms/send — отправка SMS")
    def send_sms(self, json_data: dict):
        return self.post(Url.POST_SEND_SMS, json_data=json_data)

    @allure.step("GET /sms/check — проверка кода из SMS")
    def check_sms(self, phone: str, code: str):
        return self.get(Url.GET_SMS_CHECK, params={"phone": phone, "code": code})
