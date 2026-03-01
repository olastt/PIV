import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class UserMethods(ApiClient):
    """Методы для пользователей"""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/users/{user_id} - Получение пользователя по ID")
    def get_user_by_id(self, user_id: int):
        endpoint = Url.GET_USER_BY_ID.replace("{user_id}", str(user_id))
        return self.get(endpoint)

