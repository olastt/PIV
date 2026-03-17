import allure
from base.methods.roles.roles_methods import RolesMethods


class RolesStart:
    """Стартовые сценарии для Roles."""

    def __init__(self):
        self.roles = RolesMethods()

    def get_role_by_id(self, id_role=1, params=None):
        with allure.step("Запрос роли по ID"):
            response = self.roles.get_role_by_id(id_role, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
