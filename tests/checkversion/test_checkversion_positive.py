import allure
import pytest
from Library.MakeyIS import Test


class TestCheckversionPositive:
    @pytest.mark.positive
    @allure.epic('Биллинг')
    @allure.feature('GET /api/v2/checkversion')
    @allure.title('Проверка версии приложения')
    @Test(run_test=True, group_name="Биллинг", log=True)
    def test_get_checkversion(self, checkversion_start):
        checkversion_start.get_checkversion()