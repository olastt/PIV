import allure
import pytest
from Library.MakeyIS import Test


class TestClinicPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /clinics")
    @allure.title("Просмотр информации о филиалах клиник")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_clinics(self, clinic_start):
        clinic_start.get_clinics()
