import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class CassaMethods(ApiClient):
    """Методы для касс (Cassa)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/cassa/{user_id} - Кассы пользователя")
    def get_cassa_by_user(self, user_id: int, params: dict = None):
        endpoint = Url.GET_CASSA_BY_USER.replace("{user_id}", str(user_id))
        return self.get(endpoint, params=params)
