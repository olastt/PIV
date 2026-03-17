import allure
from base.methods.tariff.tariff_methods import TariffMethods


class TariffStart:
    """Стартовые сценарии для Tariff."""

    def __init__(self):
        self.tariff = TariffMethods()

    def get_tariff(self, params=None):
        with allure.step("Запрос данных тарифа"):
            response = self.tariff.get_tariff(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
