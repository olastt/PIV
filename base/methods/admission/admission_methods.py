import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class AdmissionMethods(ApiClient):
    """Методы для приёмов (Admission)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/users/admission/{admission_id} - Приём по ID")
    def get_admission_by_id(self, admission_id: int, params: dict = None):
        endpoint = Url.GET_ADMISSION_BY_ID.replace("{admission_id}", str(admission_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/users/{user_id}/admission - Приёмы пользователя")
    def get_admissions_by_user(self, user_id: int, params: dict = None):
        endpoint = Url.GET_ADMISSIONS_BY_USER.replace("{user_id}", str(user_id))
        return self.get(endpoint, params=params)

    @allure.step("POST /api/v2/users/{user_id}/admission - Создание приёма")
    def create_admission(self, user_id: int, json_data: dict):
        endpoint = Url.POST_CREATE_ADMISSION.replace("{user_id}", str(user_id))
        return self.post(endpoint, json_data=json_data)
