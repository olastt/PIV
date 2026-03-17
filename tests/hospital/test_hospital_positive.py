import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Hospital")
class TestHospitalPositive:
    @pytest.mark.positive
    @allure.title("GET /api/v2/hospital — данные стационара")
    def test_get_hospital(self, hospital_start):
        hospital_start.get_hospital()

    @pytest.mark.positive
    @allure.title("GET /api/v2/hospital/blocks — блоки стационара")
    def test_get_hospital_blocks(self, hospital_start):
        hospital_start.get_hospital_blocks()

    @pytest.mark.positive
    @allure.title("GET /api/v2/hospital/liststatuses — статусы стационара")
    def test_get_hospital_list_statuses(self, hospital_start):
        hospital_start.get_hospital_list_statuses()

    @pytest.mark.positive
    @allure.title("GET /api/v2/hospital/{recordId} — запись стационара по ID")
    def test_get_hospital_by_id(self, hospital_start):
        hospital_start.get_hospital_by_id(record_id=1)
