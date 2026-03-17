import allure
from base.main_request_class import ApiClient
from src.config.url import Url

class ClinicMethods(ApiClient):

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/clinics - Получение всех клиник")
    def get_all_clinics(self):
        return self.get(Url.GET_CLINICS)

    @allure.step("GET /api/v2/properties - Получение настроек клиники")
    def get_clinic_properties(self):
        return self.get(Url.GET_PROPERTIES)
