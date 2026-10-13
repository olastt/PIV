import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_collection_count, assert_piv_success


class TestClinicPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /clinics")
    @allure.title("Просмотр информации о филиалах клиник")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_clinics(self, clinic_start):
        body = assert_piv_success(clinic_start.get_clinics())
        if "clinics" in body["data"]:
            assert_collection_count(body["data"], "clinics")
