import os

import allure
from base.methods.clients.clients_methods import ClientsMethods


class ClientsStart:
    """Стартовые сценарии для клиентов (Clients)."""

    def __init__(self):
        self.clients = ClientsMethods()

    def get_client_by_id(self, client_id=1):
        with allure.step("Запрос клиента по ID"):
            response = self.clients.get_client_by_id(client_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_clients_search(self, search_query="Тестович", page_number=1, page_size=20):
        params = {"search_query": search_query, "page[number]": page_number, "page[size]": page_size}
        with allure.step("Поиск клиентов"):
            response = self.clients.get_clients_search(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_client_pets(self, client_id=1, params=None):
        with allure.step("Запрос питомцев клиента"):
            response = self.clients.get_client_pets(client_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def post_client(self):
        json_data = {
            "client_data": {
                "last_name": "Тестовый",
                "first_name": "Pytest",
                "middle_name": "Тестов",
                "cell_phone": "79180052448",
                "address": "Краснодар",
                "note": "просто запись",
                "apartment": "10",
                "city_id": 252,
                "street_id": 2,
            }
        }
        with allure.step("Создание клиента"):
            response = self.clients.post_client(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response

    def patch_client(self, client_id=1, json_data: dict = None):
        if json_data is None:
            json_data = {
                "client_data": {
                    "note": "pytest patch client",
                }
            }
        with allure.step("Обновление клиента"):
            response = self.clients.patch_client(client_id, json_data)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_client_match(self, client_id=1, client_data_cell_phone="+38(232)131-23-11",
                         client_data_first_name="Тест", client_data_last_name="Тестов",
                         client_data_middle_name= "Тестович"):
        params = {
            "client_data[cell_phone]": client_data_cell_phone,
            "client_data[first_name]": client_data_first_name,
            "client_data[last_name]": client_data_last_name,
            "client_data[middle_name]": client_data_middle_name,
        }
        with allure.step("Запрос сопоставления клиента"):
            response = self.clients.get_client_match(client_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_client_contacts(self, client_id=1, params=None):
        with allure.step("Запрос контактов клиента"):
            response = self.clients.get_client_contacts(client_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_client_pet_by_id(self, client_id=1, pet_id=1, params=None):
        with allure.step("Запрос питомца клиента по ID"):
            response = self.clients.get_client_pet_by_id(client_id, pet_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    # def post_clients_combine(self, client_id_source=None, client_id_target=None, pet_id_target=0):
    #     client_id_source = client_id_source or int(os.getenv("COMBINE_CLIENT_SOURCE_ID", "2"))
    #     client_id_target = client_id_target or int(os.getenv("COMBINE_CLIENT_TARGET_ID", "1"))
    #     json_data = {
    #         "combine_data": {
    #             "client_id_source": client_id_source,
    #             "client_id_target": client_id_target,
    #             "pet_id_target": pet_id_target,
    #         }
    #     }
    #     with allure.step("Объединение клиентов (combine)"):
    #         response = self.clients.post_clients_combine(json_data)
    #     with allure.step("Проверка статус кода"):
    #         response.assert_status_code([200, 201, 422])
    #     return response

    def post_clients_combine(self, client_id_source=None, client_id_target=None, pet_id_target=0):
        client_id_source = client_id_source or int(os.getenv("COMBINE_CLIENT_SOURCE_ID", "2"))
        client_id_target = client_id_target or int(os.getenv("COMBINE_CLIENT_TARGET_ID", "1"))
        json_data = {
            "combine_data": {
                "client_id_source": client_id_source,
                "client_id_target": client_id_target,
                "pet_id_target": pet_id_target,
            }
        }
        with allure.step("POST /api/v2/clients/combine"):
            response = self.clients.post_clients_combine(json_data)
        with allure.step("Check status code"):
            response.assert_status_code([200, 201, 400, 422])
        return response
