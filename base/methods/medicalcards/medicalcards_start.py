import allure
from base.methods.medicalcards.medicalcards_methods import MedicalcardsMethods


class MedicalcardsStart:
    """Стартовые сценарии для Medicalcards."""

    def __init__(self):
        self.medicalcards = MedicalcardsMethods()

    def get_medicalcards_diagnoses(self, params=None):
        with allure.step("Запрос диагнозов для медкарт"):
            response = self.medicalcards.get_medicalcards_diagnoses(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
