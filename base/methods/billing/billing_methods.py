import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class BillingMethods(ApiClient):
    """Методы для биллинга (Billing)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/billingurl - Ссылка на биллинг")
    def get_billing_url(self):
        return self.get(Url.GET_BILLING_URL)

    @allure.step("GET /api/v2/tariff - Получение данных по тарифу")
    def get_billing_url(self):
        return self.get(Url.GET_TARIFF)
