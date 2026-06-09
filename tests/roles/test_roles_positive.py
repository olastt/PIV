import allure
import pytest
from Library.MakeyIS import Test


class TestRolesPositive:
    @pytest.mark.positive
    @allure.epic("Роли")
    @allure.feature("GET /api/v2/roles/{id_role}")
    @allure.title("Получение роли по ID")
    @Test(run_test=True, group_name="Роли", log=True)
    def test_get_role_by_id(self, roles_start):
        roles_start.get_role_by_id(id_role=1)
