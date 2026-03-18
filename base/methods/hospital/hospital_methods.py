import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class HospitalMethods(ApiClient):
    """Методы для стационара (Hospital)."""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/hospital - Данные стационара")
    def get_hospital(self, params: dict = None):
        return self.get(Url.GET_HOSPITAL, params=params)

    @allure.step("GET /api/v2/hospital/blocks - Блоки стационара")
    def get_hospital_blocks(self, params: dict = None):
        return self.get(Url.GET_HOSPITAL_BLOCKS, params=params)

    @allure.step("GET /api/v2/hospital/liststatuses - Статусы стационара")
    def get_hospital_list_statuses(self, params: dict = None):
        return self.get(Url.GET_HOSPITAL_LIST_STATUSES, params=params)

    @allure.step("GET /api/v2/hospital/{{recordId}} - Запись стационара по ID")
    def get_hospital_by_id(self, record_id: int, params: dict = None):
        endpoint = Url.GET_HOSPITAL_BY_ID.replace("{recordId}", str(record_id))
        return self.get(endpoint, params=params)

    @allure.step("PATCH /api/v2/hospital/{{recordId}} - Обновление записи стационара (UpdateHospitalByRecordId)")
    def patch_hospital_by_id(self, record_id: int, json_data: dict):
        endpoint = Url.PATCH_HOSPITAL_BY_ID.replace("{recordId}", str(record_id))
        return self.patch(endpoint, json_data=json_data)
