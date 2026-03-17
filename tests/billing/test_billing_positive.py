import allure
import pytest
from Library.MakeyIS import Test

class TestBillingPositive:
    @pytest.mark.positive
    @allure.epic('Биллинг')
    @allure.feature('GET /api/v2/billingurl')
    @allure.title('Получение ссылки перехода в биллинг')
    @Test(run_test=True, group_name="Биллинг", log=True)
    def test_get_billing_url(self, billing_start):
        billing_start.get_billing_url()
