import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class PetsMethods(ApiClient):
    """Методы для питомцев и справочников (Pets, Types, Genders, Breeds по Swagger)"""

    def __init__(self):
        super().__init__()

    @allure.step("GET /api/v2/pets/types - Типы питомцев")
    def get_pets_types(self, params: dict = None):
        return self.get(Url.GET_PETS_TYPES, params=params)

    @allure.step("GET /api/v2/pets/genders - Пол питомцев")
    def get_pets_genders(self, params: dict = None):
        return self.get(Url.GET_PETS_GENDERS, params=params)

    @allure.step("GET /api/v2/pets/types/{type_id}/breeds - Породы по типу")
    def get_breeds_by_type(self, type_id: int):
        endpoint = Url.GET_BREEDS_BY_TYPE.replace("{type_id}", str(type_id))
        return self.get(endpoint)

    @allure.step("GET /api/v2/pets/breeds - Все породы")
    def get_pets_breeds(self, params: dict = None):
        return self.get(Url.GET_PETS_BREEDS, params=params)

    @allure.step("GET /api/v2/clients/{client_id}/pets/{pet_id} - Питомец по ID")
    def get_pet_by_client(self, client_id: int, pet_id: int):
        endpoint = Url.GET_PET_BY_CLIENT.replace("{client_id}", str(client_id)).replace("{pet_id}", str(pet_id))
        return self.get(endpoint)
