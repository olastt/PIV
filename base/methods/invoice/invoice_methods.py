import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class InvoiceMethods(ApiClient):

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/clients/{client_id}/invoices - Счета клиента")
    def get_client_invoices(self, client_id: int):
        endpoint = Url.GET_CLIENT_INVOICES.replace("{client_id}", str(client_id))
        return self.get(endpoint)

    @allure.step(
        "GET /api/v2/clients/{{client_id}}/invoices/{{invoice_id}}/products - Товары по счёту (ProductsByInvoice)")
    def get_client_invoice_products(self, client_id: int, invoice_id: int, params: dict = None):
        endpoint = (
            Url.GET_CLIENT_INVOICE_PRODUCTS.replace("{client_id}", str(client_id)).replace(
                "{invoice_id}", str(invoice_id)
            )
        )
        return self.get(endpoint, params=params)

    @allure.step("POST /api/v2/clients/{{client_id}}/payments - Оплата счёта (PayInvoice)")
    def post_client_payments(self, client_id: int, json_data: dict):
        endpoint = Url.POST_CLIENT_PAYMENTS.replace("{client_id}", str(client_id))
        return self.post(endpoint, json_data=json_data)

    @allure.step("POST /api/v2/clients/{client_id}/invoices — создание счёта (form-urlencoded)")
    def post_client_invoice(self, client_id: int, data: dict):
        endpoint = Url.POST_CLIENT_INVOICES.replace("{client_id}", str(client_id))
        return self.post(
            endpoint,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
