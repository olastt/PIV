import allure
from base.methods.pets.pets_methods import PetsMethods


class PetsStart:
    """Стартовые сценарии для питомцев и справочников (Pets, Types, Genders, Breeds)."""

    def __init__(self):
        self.pets = PetsMethods()

    def get_pets_types(self, params=None):
        with allure.step("Запрос типов питомцев"):
            response = self.pets.get_pets_types(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_pets_genders(self, params=None):
        with allure.step("Запрос полов питомцев"):
            response = self.pets.get_pets_genders(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_breeds_by_type(self, type_id=1):
        with allure.step("Запрос пород по типу"):
            response = self.pets.get_breeds_by_type(type_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_pets_breeds(self, params=None):
        with allure.step("Запрос списка пород"):
            response = self.pets.get_pets_breeds(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_pet_by_client(self, client_id=1, pet_id=1, params=None):
        with allure.step("Запрос питомца по ID клиента и питомца"):
            response = self.pets.get_pet_by_client(client_id, pet_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
