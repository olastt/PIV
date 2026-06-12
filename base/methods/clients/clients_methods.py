import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class ClientsMethods(PivApiClient):
    @allure.step("GET /clients/clientByPhone — клиент по номеру телефона")
    def get_client_by_phone(self, phone: str):
        return self.get(Url.GET_CLIENT_BY_PHONE, params={"phone": str(phone)})
