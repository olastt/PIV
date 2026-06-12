import os

import allure

from base.methods.medicalcards.medicalcards_methods import MedicalcardsMethods


class MedicalcardsStart:
    def __init__(self):
        self.medicalcards = MedicalcardsMethods()

    def get_recomendations(self, client_id=None):
        client_id = client_id or int(os.getenv("CLIENT_ID", "6"))
        with allure.step("GET /medicalCards/recomendations"):
            response = self.medicalcards.get_recomendations(client_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_vaccinations(self, client_id=None):
        client_id = client_id or int(os.getenv("CLIENT_ID", "6"))
        with allure.step("GET /medicalCards/vaccinations"):
            response = self.medicalcards.get_vaccinations(client_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
