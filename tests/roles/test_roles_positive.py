import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Roles")
class TestRolesPositive:
    @pytest.mark.positive
    @allure.title("GET /api/v2/roles/{id_role} — роль по ID")
    def test_get_role_by_id(self, roles_start):
        roles_start.get_role_by_id(id_role=1)
