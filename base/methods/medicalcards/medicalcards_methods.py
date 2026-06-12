import allure

from base.piv_client import PivApiClient
from src.config.url import Url


class MedicalcardsMethods(PivApiClient):
    @allure.step("GET /medicalCards/recomendations — рекомендации клиента")
    def get_recomendations(self, client_id: int):
        return self.get(Url.GET_RECOMENDATIONS_BY_CLIENT_ID, params={"client_id": client_id})

    @allure.step("GET /medicalCards/vaccinations — вакцинации клиента")
    def get_vaccinations(self, client_id: int):
        return self.get(Url.GET_VACCINATIONS_BY_CLIENT_ID, params={"client_id": client_id})
