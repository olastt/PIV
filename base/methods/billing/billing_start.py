import allure
from base.methods.billing.billing_methods import BillingMethods


class BillingStart:
    """Стартовые сценарии для Billing."""

    def __init__(self):
        self.billing = BillingMethods()

    def get_billing_url(self):
        with allure.step("Запрос ссылки на биллинг"):
            response = self.billing.get_billing_url()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_billing_tariff(self):
        with allure.step("Запрос ссылки на биллинг"):
            response = self.billing.get_billing_url()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

