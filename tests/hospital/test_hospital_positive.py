import allure
import pytest
from Library.MakeyIS import Test


class TestHospitalPositive:

    @pytest.mark.positive
    @allure.epic('Стационар')
    @allure.feature('GET /api/v2/hospital')
    @allure.title('Получение данных по статционару')
    @Test(run_test=True, group_name="Стационар", log=True)
    def test_get_hospital(self, hospital_start):
        hospital_start.get_hospital()

    @pytest.mark.positive
    @allure.epic('Стационар')
    @allure.feature('GET /api/v2/hospital/blocks')
    @allure.title('Получение списка блоков для стационара')
    @Test(run_test=True, group_name="Стационар", log=True)
    def test_get_hospital_blocks(self, hospital_start):
        hospital_start.get_hospital_blocks()

    @pytest.mark.positive
    @allure.epic('Стационар')
    @allure.feature('GET /api/v2/hospital/liststatuses')
    @allure.title('Получение списка статусов для записей стационара')
    @Test(run_test=True, group_name="Стационар", log=True)
    def test_get_hospital_list_statuses(self, hospital_start):
        hospital_start.get_hospital_list_statuses()

    @pytest.mark.positive
    @allure.epic('Стационар')
    @allure.feature('GET /api/v2/hospital/{recordId}')
    @allure.title('Получение данных по записи стационара')
    @Test(run_test=True, group_name="Стационар", log=True)
    def test_get_hospital_by_id(self, hospital_start):
        hospital_start.get_hospital_by_id()

    @pytest.mark.positive
    @allure.epic('Стационар')
    @allure.feature('PATCH /api/v2/hospital/{recordId}')
    @allure.title('Обновление данных записи стационара')
    @Test(run_test=True, group_name="Стационар", log=True)
    def test_update_hospital_by_record_id(self, hospital_start):
        hospital_start.update_hospital_by_record_id()
