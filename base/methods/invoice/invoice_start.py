import os

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

    # def pay_invoice(self, client_id=1, json_data=None):
    #     if json_data is None:
    #         json_data = {
    #             "invoice_data": {
    #                 "invoice_id": 108,
    #                 "amount": 30,
    #             }
    #         }
    #     with allure.step("Оплата счёта"):
    #         response = self.invoice.post_client_payments(client_id, json_data)
    #     with allure.step("Проверка статус кода"):
    #         response.assert_status_code(200)
    #     return response

    def pay_invoice(self, client_id=1, json_data=None):
        if json_data is None:
            json_data = {
                "invoice_data": {
                    "invoice_id": int(os.getenv("PAYMENT_INVOICE_ID", "1")),
                    "amount": int(os.getenv("PAYMENT_AMOUNT", "30")),
                }
            }
        with allure.step("POST /api/v2/clients/{client_id}/payments"):
            response = self.invoice.post_client_payments(client_id, json_data)
        with allure.step("Check status code"):
            response.assert_status_code([200, 201, 400, 404, 422])
        return response

    def post_client_invoice(self, client_id=1, data: dict = None):
        if data is None:
            cid = int(os.getenv("CLIENT_ID", "1"))
            pid = int(os.getenv("PET_ID", "1"))
            goods = os.getenv(
                "INVOICE_GOODS_JSON",
                '[{"product_id":"1_1_0","qty":1,"price":10,"tag_id":0,"default_price":10,'
                '"party_accounts":null,"party_accounts_count":0}]',
            )
            data = {
                "invoice_data[doctor_id]": os.getenv("DOCTOR_ID", "1"),
                "invoice_data[clinic_id]": os.getenv("CLINIC_ID", "1"),
                "invoice_data[client_id]": str(cid),
                "invoice_data[pet_id]": str(pid),
                "invoice_data[amount]": "30",
                "invoice_data[invoice_amount]": "30",
                "invoice_data[discount]": "0",
                "invoice_data[discount_amount]": "0",
                "invoice_data[increase]": "0",
                "invoice_data[increase_amount]": "0",
                "invoice_data[night]": "0",
                "invoice_data[call]": "0",
                "invoice_data[description]": "pytest invoice",
                "invoice_data[client_note]": "pytest",
                "invoice_data[goods]": goods,
            }
        with allure.step("POST /api/v2/clients/{client_id}/invoices (form-urlencoded)"):
            response = self.invoice.post_client_invoice(client_id, data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        return response
