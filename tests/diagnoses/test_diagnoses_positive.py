import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Diagnoses")
class TestDiagnosesPositive:
    @pytest.mark.positive
    @allure.title("GET /api/v2/diagnoses — список диагнозов")
    def test_get_diagnoses(self, diagnoses_start):
        diagnoses_start.get_diagnoses()

    @pytest.mark.positive
    @allure.title("GET /api/v2/diagnoses/{diagnos_id} — диагноз по ID")
    def test_get_diagnos_by_id(self, diagnoses_start):
        diagnoses_start.get_diagnos_by_id(diagnos_id=1)
