import allure
import pytest
from Library.MakeyIS import Test


class TestTariffPositive:
    @pytest.mark.positive
    @allure.epic("Тариф")
    @allure.feature("GET /api/v2/tariff")
    @allure.title("Получение данных по тарифу")
    @Test(run_test=True, group_name="Тариф", log=True)
    def test_get_tariff(self, tariff_start):
        tariff_start.get_tariff()
