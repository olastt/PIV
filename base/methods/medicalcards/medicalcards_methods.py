import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class MedicalcardsMethods(ApiClient):
    """Методы для медкарт (Medicalcards, Vaccinations по Postman)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/clients/medicalcards/diagnoses - Диагнозы для медкарт")
    def get_medicalcards_diagnoses(self, params: dict = None):
        return self.get(Url.GET_DIAGNOSES_FOR_MEDICALCARDS, params=params)

    @allure.step("GET /api/v2/medicalcards/vaccinations/{pet_id} - Вакцинации по питомцу")
    def get_vaccinations_by_pet(self, pet_id: int, params: dict = None):
        endpoint = Url.GET_VACCINATIONS_BY_PET.replace("{pet_id}", str(pet_id))
        return self.get(endpoint, params=params)

    @allure.step("POST /api/v2/medicalcards/{medicalcard_id}/vaccinations/{pet_id}")
    def post_medicalcard_vaccination(self, medicalcard_id: int, pet_id: int, json_data: dict):
        endpoint = (
            Url.POST_MEDICALCARD_VACCINATION.replace("{medicalcard_id}", str(medicalcard_id)).replace(
                "{pet_id}", str(pet_id)
            )
        )
        return self.post(endpoint, json_data=json_data)

    @allure.step("PATCH /api/v2/medicalcards/{medicalcard_id}/vaccinations/{vaccination_id}")
    def patch_medicalcard_vaccination(self, medicalcard_id: int, vaccination_id: int, json_data: dict):
        endpoint = (
            Url.PATCH_MEDICALCARD_VACCINATION.replace("{medicalcard_id}", str(medicalcard_id)).replace(
                "{vaccination_id}", str(vaccination_id)
            )
        )
        return self.patch(endpoint, json_data=json_data)

    @allure.step("PATCH /api/v2/medicalcards/vaccinations/{vaccination_id}")
    def patch_medicalcard_vaccination_short(self, vaccination_id: int, json_data: dict):
        endpoint = Url.PATCH_MEDICALCARD_VACCINATION_SHORT.replace("{vaccination_id}", str(vaccination_id))
        return self.patch(endpoint, json_data=json_data)

    @allure.step("GET /api/v2/clients/{client_id}/medicalcards")
    def get_medicalcards_by_client(self, client_id: int, params: dict = None):
        endpoint = Url.GET_MEDICALCARDS_BY_CLIENT.replace("{client_id}", str(client_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/clients/{client_id}/medicalcards/{medicalcard_id}")
    def get_medicalcard_by_client(self, client_id: int, medicalcard_id: int, params: dict = None):
        endpoint = (
            Url.GET_MEDICALCARD_BY_CLIENT.replace("{client_id}", str(client_id)).replace(
                "{medicalcard_id}", str(medicalcard_id)
            )
        )
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/medicalcards/texttemplates")
    def get_medicalcard_text_templates(self, params: dict = None):
        return self.get(Url.GET_MEDICALCARD_TEXT_TEMPLATES, params=params)

    @allure.step("GET /api/v2/clients/{client_id}/medicalcards/history")
    def get_medicalcards_history(self, client_id: int, params: dict = None):
        endpoint = Url.GET_MEDICALCARDS_HISTORY.replace("{client_id}", str(client_id))
        return self.get(endpoint, params=params)

    @allure.step("POST /api/v2/medicalcards/uploadfiles")
    def post_medicalcards_uploadfiles(self, json_data: dict = None):
        return self.post(Url.POST_MEDICALCARDS_UPLOADFILES, json_data=json_data or {})

    @allure.step("POST /api/v2/medicalcards/generate-llm")
    def post_medicalcards_generate_llm(self, json_data: dict):
        return self.post(Url.POST_MEDICALCARDS_GENERATE_LLM, json_data=json_data)

    @allure.step("POST /api/v2/clients/{client_id}/medicalcards")
    def post_create_medicalcard(self, client_id: int, json_data: dict):
        endpoint = Url.POST_CREATE_MEDICALCARD.replace("{client_id}", str(client_id))
        return self.post(endpoint, json_data=json_data)

    @allure.step("PATCH /api/v2/clients/{client_id}/medicalcards/{medicalcard_id}")
    def patch_medicalcard(self, client_id: int, medicalcard_id: int, json_data: dict):
        endpoint = (
            Url.PATCH_MEDICALCARD.replace("{client_id}", str(client_id)).replace(
                "{medicalcard_id}", str(medicalcard_id)
            )
        )
        return self.patch(endpoint, json_data=json_data)
