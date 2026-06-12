import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class ClinicsMethods(PivApiClient):
    @allure.step("GET /clinics — филиалы клиники")
    def get_clinics(self):
        return self.get(Url.GET_CLINICS)
