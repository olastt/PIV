import os

import allure

from base.methods.piv_admissions.piv_admissions_methods import PivAdmissionsMethods


class PivAdmissionsStart:
    def __init__(self):
        self.admissions = PivAdmissionsMethods()

    def get_admissions_by_client_id(self, client_id=None):
        client_id = client_id or int(os.getenv("CLIENT_ID", "6"))
        with allure.step("GET /admissions"):
            response = self.admissions.get_admissions_by_client_id(client_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
