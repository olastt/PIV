import allure
import pytest
from Library.MakeyIS import Test


class TestDiagnosesPositive:

    @pytest.mark.positive
    @allure.epic('Диагнозы')
    @allure.feature('GET /api/v2/diagnoses')
    @allure.title('Получение списка всех диагнозов')
    @Test(run_test=True, group_name="Диагнозы", log=True)
    def test_get_diagnoses(self, diagnoses_start):
        diagnoses_start.get_diagnoses()

    @pytest.mark.positive
    @allure.epic('Диагнозы')
    @allure.feature('GET /api/v2/diagnoses/{diagnos_id}')
    @allure.title('Получение данных по диагнозу')
    @Test(run_test=True, group_name="Диагнозы", log=True)
    def test_get_diagnos_by_id(self, diagnoses_start):
        diagnoses_start.get_diagnos_by_id(diagnos_id=1)

    @pytest.mark.positive
    @allure.epic('Диагнозы')
    @allure.feature('POST /api/v2/diagnoses')
    @allure.title('Создание диагноза')
    @Test(run_test=True, group_name="Диагнозы", log=True)
    def test_create_diagnos(self, diagnoses_start):
        diagnoses_start.create_diagnos()

    @pytest.mark.positive
    @allure.epic('Диагнозы')
    @allure.feature('PATCH /api/v2/diagnoses/{diagnos_id}')
    @allure.title('Обновление диагноза')
    @Test(run_test=True, group_name="Диагнозы", log=True)
    def test_update_diagnos(self, diagnoses_start):
        diagnoses_start.update_diagnos()

    @pytest.mark.positive
    @allure.epic('Диагнозы')
    @allure.feature('DELETE /api/v2/diagnoses/{diagnos_id}')
    @allure.title('Удаление диагноза')
    @Test(run_test=True, group_name="Диагнозы", log=True)
    def test_delete_diagnos(self, diagnoses_start):
        diagnoses_start.delete_diagnos()
