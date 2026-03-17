import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class DiagnosesMethods(ApiClient):
    """Методы для диагнозов (Diagnoses)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/diagnoses - Список диагнозов")
    def get_diagnoses(self, params: dict = None):
        return self.get(Url.GET_DIAGNOSES, params=params)

    @allure.step("GET /api/v2/diagnoses/{diagnos_id} - Диагноз по ID")
    def get_diagnos_by_id(self, diagnos_id: int, params: dict = None):
        endpoint = Url.GET_DIAGNOS_BY_ID.replace("{diagnos_id}", str(diagnos_id))
        return self.get(endpoint, params=params)
