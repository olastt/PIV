import allure
import pytest
from Library.MakeyIS import Test



class TestCallsPositive:
    @pytest.mark.positive
    @allure.epic('Звонки')
    @allure.feature('GET /api/v2/users/{user_id}/calls')
    @allure.title('Получение прозвонов, которые должен совершить пользователь')
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_get_user_calls(self, calls_start):
        calls_start.get_user_calls(user_id=1)

    @pytest.mark.positive
    @allure.epic('Звонки')
    @allure.feature('GET /api/v2/calls/search')
    @allure.title('Поиск выполненных звонков')
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_get_calls_search(self, calls_start):
        calls_start.get_calls_search()
