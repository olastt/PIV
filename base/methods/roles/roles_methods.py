import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class RolesMethods(ApiClient):
    """Методы для ролей (Roles)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/roles/{id_role} - Роль по ID")
    def get_role_by_id(self, id_role: int, params: dict = None):
        endpoint = Url.GET_ROLE_BY_ID.replace("{id_role}", str(id_role))
        return self.get(endpoint, params=params)
