import allure
import pytest
from Library.MakeyIS import Test


class TestUser:

    @pytest.mark.positive
    @allure.epic('Пользователи')
    @allure.feature('GET /api/v2/users/')
    @allure.title('Получение пользователя по ID')
    @Test(run_test=True, group_name="Пользователи", log=True)
    def test_get_user_by_id(self, user_start):
        user_start.get_user_by_id()