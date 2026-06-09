import allure
import pytest
from Library.MakeyIS import Test


class TestCallsPositive:
    @pytest.mark.positive
    @allure.epic("Звонки")
    @allure.feature("GET /api/v2/users/{user_id}/calls")
    @allure.title("Получение прозвонов пользователя")
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_get_user_calls(self, calls_start):
        calls_start.get_user_calls()

    @pytest.mark.positive
    @allure.epic("Звонки")
    @allure.feature("GET /api/v2/calls/search")
    @allure.title("Поиск выполненных звонков")
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_get_calls_search(self, calls_start):
        calls_start.get_calls_search()

    @pytest.mark.positive
    @allure.epic("Звонки")
    @allure.feature("POST /api/v2/users/{user_id}/calls")
    @allure.title("Создание прозвона")
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_create_user_call(self, calls_start):
        calls_start.create_user_call()

    @pytest.mark.positive
    @allure.epic("Звонки")
    @allure.feature("PATCH /api/v2/users/{user_id}/calls/{call_id}")
    @allure.title("Обновление прозвона")
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_update_user_call(self, calls_start, call_for_update):
        calls_start.update_user_call()

    @pytest.mark.positive
    @allure.epic("Звонки")
    @allure.feature("GET /api/v2/users/{user_id}/calls/{call_id}")
    @allure.title("Получение прозвона по ID")
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_get_user_call_by_id(self, calls_start):
        calls_start.get_user_call_by_id()
