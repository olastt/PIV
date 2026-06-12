import allure
import pytest
from Library.MakeyIS import Test


class TestDomainNamePositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /domainName")
    @allure.title("Получение доменного имени клиники")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_domain_name(self, domain_name_start):
        domain_name_start.get_domain_name()
