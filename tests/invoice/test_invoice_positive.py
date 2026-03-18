import allure
import pytest
from Library.MakeyIS import Test

class TestInvoicePositive:

    @pytest.mark.positive
    @allure.epic('Счета')
    @allure.feature('GET /api/v2/clients/{client_id}/invoices')
    @allure.title("Получение информации о счетах клиента")
    @Test(run_test=True, group_name="Счета", log=True)
    def test_get_client_invoices(self, invoice_start):
        invoice_start.get_client_invoice()

    @pytest.mark.positive
    @allure.epic('Счета')
    @allure.feature('GET /api/v2/clients/{client_id}/invoices/{invoice_id}/products')
    @allure.title('Продукты в счете')
    @Test(run_test=True, group_name="Счета", log=True)
    def test_products_by_invoice(self, invoice_start):
        invoice_start.get_products_by_invoice()

    @pytest.mark.positive
    @allure.epic('Счета')
    @allure.feature('POST /api/v2/clients/{client_id}/payments')
    @allure.title('Оплата инвойса')
    @Test(run_test=True, group_name="Счета", log=True)
    def test_pay_invoice(self, invoice_start):
        invoice_start.pay_invoice()