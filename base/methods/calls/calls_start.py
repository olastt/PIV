import allure
from base.methods.calls.calls_methods import CallsMethods


class CallsStart:
    """Стартовые сценарии для Calls."""

    def __init__(self):
        self.calls = CallsMethods()

    def get_user_calls(self, user_id=1, params=None):
        with allure.step("Запрос прозвонов пользователя"):
            response = self.calls.get_user_calls(user_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_calls_search(self, params=None):
        with allure.step("Запрос поиска прозвонов"):
            response = self.calls.get_calls_search(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
