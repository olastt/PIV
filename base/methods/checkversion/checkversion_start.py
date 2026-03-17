import allure
from base.methods.checkversion.checkversion_methods import CheckversionMethods


class CheckversionStart:
    """Стартовые сценарии для Checkversion."""

    def __init__(self):
        self.checkversion = CheckversionMethods()

    def get_checkversion(self, params=None):
        with allure.step("Запрос проверки версии"):
            response = self.checkversion.get_checkversion(params=params)
            print(response)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
