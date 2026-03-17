import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class CallsMethods(ApiClient):
    """Методы для прозвонов (Calls)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/users/{user_id}/calls - Прозвоны пользователя")
    def get_user_calls(self, user_id: int, params: dict = None):
        endpoint = Url.GET_USER_CALLS.replace("{user_id}", str(user_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/calls/search - Поиск прозвонов")
    def get_calls_search(self, params: dict = None):
        return self.get(Url.GET_CALLS_SEARCH, params=params)
