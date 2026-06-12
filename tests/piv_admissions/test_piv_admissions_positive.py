import allure
import pytest
from Library.MakeyIS import Test


class TestPivAdmissionsPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /admissions")
    @allure.title("Получение списка визитов клиента")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_admissions_by_client_id(self, piv_admissions_start):
        piv_admissions_start.get_admissions_by_client_id()
