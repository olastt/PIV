import allure
import pytest
from Library.MakeyIS import Test


class TestInvoicePositive:
    @pytest.mark.positive
    @allure.feature("GET /api/v2/clients/{client_id}/invoices")
    @Test(run_test=True, group_name="Invoice", log=True)
    def test_get_client_invoices(self, invoice_start):
        invoice_start.get_client_invoice()

    @pytest.mark.positive
    @allure.feature("GET /api/v2/clients/{client_id}/invoices/{invoice_id}/products")
    @Test(run_test=True, group_name="Invoice", log=True)
    def test_products_by_invoice(self, invoice_start):
        invoice_start.get_products_by_invoice()

    @pytest.mark.positive
    @allure.feature("POST /api/v2/clients/{client_id}/payments")
    @Test(run_test=True, group_name="Invoice", log=True)
    def test_pay_invoice(self, invoice_start):
        invoice_start.pay_invoice()

    @pytest.mark.positive
    @allure.feature("POST /api/v2/clients/{client_id}/invoices")
    @Test(run_test=True, group_name="Invoice", log=True)
    def test_post_create_invoice(self, invoice_start):
        invoice_start.post_client_invoice()
