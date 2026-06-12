import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class PivAdmissionsMethods(PivApiClient):
    @allure.step("GET /admissions — визиты клиента")
    def get_admissions_by_client_id(self, client_id: int):
        return self.get(Url.GET_ADMISSIONS_BY_CLIENT_ID, params={"client_id": client_id})
