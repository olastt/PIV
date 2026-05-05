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

    def post_client_pet(self, client_id=1, json_data: dict = None):
        if json_data is None:
            json_data = {
                "pet_data": {
                    "alias": "pytest_pet",
                    "pet_type": 2,
                    "breed_id": 2,
                    "sex": "male",
                    "birthdate": "2026-03-01",
                    "note": "тестовая заметка",
                    "chip_number": 12345678901234567890123456789012,
                }
            }
        with allure.step("POST /api/v2/clients/{client_id}/pets"):
            response = self.pets.post_client_pet(client_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201])
        return response

    def patch_client_pet(self, client_id=1, pet_id=1, json_data: dict = None):
        if json_data is None:
            json_data = {"pet_data": {"note": "patched from pytest"}}
        with allure.step("PATCH /api/v2/clients/{client_id}/pets/{pet_id}"):
            response = self.pets.patch_client_pet(client_id, pet_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201])
        return response
