import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class TariffMethods(ApiClient):
    """Методы для тарифа (Tariff)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/tariff - Данные тарифа")
    def get_tariff(self, params: dict = None):
        return self.get(Url.GET_TARIFF, params=params)
