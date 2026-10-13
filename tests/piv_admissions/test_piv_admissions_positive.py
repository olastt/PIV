import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_collection_count, assert_piv_success


class TestPivAdmissionsPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /admissions")
    @allure.title("Получение списка визитов клиента")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_admissions_by_client_id(self, piv_admissions_start):
        body = assert_piv_success(piv_admissions_start.get_admissions_by_client_id())
        assert_collection_count(body["data"], "admission")
