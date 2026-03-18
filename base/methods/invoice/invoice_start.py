import allure
from base.methods.invoice.invoice_methods import InvoiceMethods

class InvoiceStart:

    def __init__(self):
        self.invoice = InvoiceMethods()

    def get_client_invoice(self, client_id=1):
        with allure.step("Запрос счетов клиента"):
            response = self.invoice.get_client_invoices(client_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_products_by_invoice(self, client_id=1, invoice_id=1, params=None):
        with allure.step("Запрос товаров по счёту (ProductsByInvoice)"):
            response = self.invoice.get_client_invoice_products(client_id, invoice_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def pay_invoice(self, client_id=1, json_data=None):
        if json_data is None:
            json_data = {
                "invoice_data": {
                    "invoice_id": 108,
                    "amount": 30,
                }
            }
        with allure.step("Оплата счёта (PayInvoice)"):
            response = self.invoice.post_client_payments(client_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response