import allure
from base.methods.clients.clients_methods import ClientsMethods


class ClientsStart:
    """Стартовые сценарии для клиентов (Clients)."""

    def __init__(self):
        self.clients = ClientsMethods()

    def get_client_by_id(self, client_id=1):
        with allure.step("Запрос клиента по ID"):
            response = self.clients.get_client_by_id(client_id)
            print(response)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_clients_search(self, search_query="Петров", page_number=1, page_size=20):
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

    def get_client_invoices(self, client_id=1):
        with allure.step("Запрос счетов клиента"):
            response = self.clients.get_client_invoices(client_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def post_client(self, json_data: dict):
        with allure.step("Создание клиента"):
            response = self.clients.post_client(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(201)
        return response

    def patch_client(self, client_id=1, json_data: dict = None):
        with allure.step("Обновление клиента"):
            response = self.clients.patch_client(client_id, json_data or {})
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
