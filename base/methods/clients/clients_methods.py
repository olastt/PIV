import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class ClientsMethods(ApiClient):
    """Методы для клиентов (Clients по Swagger)"""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/clients/{client_id} - Получение клиента по ID")
    def get_client_by_id(self, client_id: int):
        endpoint = Url.GET_CLIENT_BY_ID.replace("{client_id}", str(client_id))
        return self.get(endpoint)

    @allure.step("PATCH /api/v2/clients/{client_id} - Обновление клиента")
    def patch_client(self, client_id: int, json_data: dict):
        endpoint = Url.PATCH_CLIENT.replace("{client_id}", str(client_id))
        return self.patch(endpoint, json_data=json_data)

    @allure.step("GET /api/v2/clients/search/ - Поиск клиентов")
    def get_clients_search(self, params: dict):
        return self.get(Url.GET_CLIENTS_SEARCH, params=params)

    @allure.step("POST /api/v2/clients - Создание клиента")
    def post_client(self, json_data: dict):
        return self.post(Url.POST_CLIENTS, json_data=json_data)

    @allure.step("GET /api/v2/clients/{client_id}/pets - Питомцы клиента")
    def get_client_pets(self, client_id: int, params: dict = None):
        endpoint = Url.GET_CLIENT_PETS.replace("{client_id}", str(client_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/clients/{client_id}/match - Сопоставление клиента (ClientsMatch)")
    def get_client_match(self, client_id: int, params: dict = None):
        endpoint = Url.GET_CLIENT_MATCH.replace("{client_id}", str(client_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/clients/{client_id}/contacts - Контакты клиента (ContactsInfoByClient)")
    def get_client_contacts(self, client_id: int, params: dict = None):
        endpoint = Url.GET_CLIENT_CONTACTS.replace("{client_id}", str(client_id))
        return self.get(endpoint, params=params)

    @allure.step("GET /api/v2/clients/{client_id}/pets/{pet_id} - Питомец клиента по ID (PetInfoByClient)")
    def get_client_pet_by_id(self, client_id: int, pet_id: int, params: dict = None):
        endpoint = (
            Url.GET_CLIENT_PET_BY_ID.replace("{client_id}", str(client_id)).replace("{pet_id}", str(pet_id))
        )
        return self.get(endpoint, params=params)

    @allure.step("POST /api/v2/clients/combine - Объединение клиентов")
    def post_clients_combine(self, json_data: dict):
        return self.post(Url.POST_CLIENTS_COMBINE, json_data=json_data)


