import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class CheckversionMethods(ApiClient):
    """Методы для проверки версии приложения (Checkversion)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/checkversion - Проверка версии приложения")
    def get_checkversion(self, params: dict = None):
        return self.get(Url.GET_CHECKVERSION, params=params)
