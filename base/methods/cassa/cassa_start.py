import allure
from base.methods.cassa.cassa_methods import CassaMethods


class CassaStart:
    """Стартовые сценарии для Cassa."""

    def __init__(self):
        self.cassa = CassaMethods()

    def get_cassa_by_user(self, user_id=1, params=None):
        with allure.step("Запрос касс пользователя"):
            response = self.cassa.get_cassa_by_user(user_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
