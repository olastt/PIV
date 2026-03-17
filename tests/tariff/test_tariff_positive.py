import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Tariff")
class TestTariffPositive:
    @pytest.mark.positive
    @allure.title("GET /api/v2/tariff — данные тарифа")
    def test_get_tariff(self, tariff_start):
        tariff_start.get_tariff()
