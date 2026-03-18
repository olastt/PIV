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

    @allure.step("POST /api/v2/users/{user_id}/calls - Создание прозвона")
    def create_user_call(self, user_id: int, json_data: dict):
        endpoint = Url.POST_CREATE_USER_CALL.replace("{user_id}", str(user_id))
        return self.post(endpoint, json_data=json_data)

    @allure.step("PATCH /api/v2/users/{user_id}/calls/{call_id} - Обновление прозвона")
    def update_user_call(self, user_id: int, call_id: int, json_data: dict):
        endpoint = (
            Url.PUT_UPDATE_USER_CALL.replace("{user_id}", str(user_id)).replace("{call_id}", str(call_id))
        )
        return self.patch(endpoint, json_data=json_data)

    @allure.step("GET /api/v2/users/{user_id}/calls/{call_id} - Прозвон по ID")
    def get_user_call_by_id(self, user_id: int, call_id: int, params: dict = None):
        endpoint = (
            Url.GET_USER_CALL_BY_ID.replace("{user_id}", str(user_id)).replace("{call_id}", str(call_id))
        )
        return self.get(endpoint, params=params)
