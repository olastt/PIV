import allure
import pytest
from Library.MakeyIS import Test


class TestCassaPositive:
    @pytest.mark.positive
    @allure.epic('Касса')
    @allure.feature('GET /api/v2/cassa/{user_id}')
    @allure.title('Получение списка касс для пользователя')
    @Test(run_test=True, group_name="Касса", log=True)
    def test_get_cassa_by_user(self, cassa_start):
        cassa_start.get_cassa_by_user(user_id=1)