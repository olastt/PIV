import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class PhonePrefixMethods(PivApiClient):
    @allure.step("GET /getPhonePrefix — префикс телефона")
    def get_phone_prefix(self):
        return self.get(Url.GET_PHONE_PREFIX)
