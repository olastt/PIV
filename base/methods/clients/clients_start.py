import os

import allure

from base.methods.clients.clients_methods import ClientsMethods


class ClientsStart:
    def __init__(self):
        self.clients = ClientsMethods()

    def get_client_by_phone(self, phone=None):
        phone = phone or os.getenv("CLIENT_PHONE", "9184140259")
        phone = str(phone)
        with allure.step("GET /clients/clientByPhone"):
            response = self.clients.get_client_by_phone(phone)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
