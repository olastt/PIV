import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Medicalcards")
class TestMedicalcardsPositive:
    @pytest.mark.positive
    @allure.title("GET /api/v2/clients/medicalcards/diagnoses — диагнозы для медкарт")
    def test_get_medicalcards_diagnoses(self, medicalcards_start):
        medicalcards_start.get_medicalcards_diagnoses()
