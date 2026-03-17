import allure
from base.methods.billing.billing_methods import BillingMethods


class BillingStart:
    """Стартовые сценарии для Billing."""

    def __init__(self):
        self.billing = BillingMethods()

    def get_billing_url(self, params=None):
        with allure.step("Запрос ссылки на биллинг"):
            response = self.billing.get_billing_url(params=params)
            print(response)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
