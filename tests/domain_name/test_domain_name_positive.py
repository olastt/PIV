import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_nonempty_string, assert_piv_success


class TestDomainNamePositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /domainName")
    @allure.title("Получение доменного имени клиники")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_domain_name(self, domain_name_start):
        body = assert_piv_success(domain_name_start.get_domain_name())
        assert_nonempty_string(body["data"]["domain_name"], "data.domain_name")
