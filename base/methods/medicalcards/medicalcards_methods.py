import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class MedicalcardsMethods(ApiClient):
    """Методы для медкарт (Medicalcards)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/clients/medicalcards/diagnoses - Диагнозы для медкарт")
    def get_medicalcards_diagnoses(self, params: dict = None):
        return self.get(Url.GET_DIAGNOSES_FOR_MEDICALCARDS, params=params)
