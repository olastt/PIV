# Тесты по Swagger: Pets (типы, пол, породы)
import allure
import pytest


@allure.epic("API по Swagger")
@allure.feature("Pets / Types / Genders / Breeds")
class TestPetsPositive:

    @pytest.mark.positive
    @allure.title("GET /api/v2/pets/types — типы питомцев")
    def test_get_pets_types(self, pets_start):
        pets_start.get_pets_types()

    @pytest.mark.positive
    @allure.title("GET /api/v2/pets/genders — пол питомцев")
    def test_get_pets_genders(self, pets_start):
        pets_start.get_pets_genders()

    @pytest.mark.positive
    @allure.title("GET /api/v2/pets/types/{type_id}/breeds — породы по типу")
    def test_get_breeds_by_type(self, pets_start):
        pets_start.get_breeds_by_type(type_id=1)

    @pytest.mark.positive
    @allure.title("GET /api/v2/pets/breeds — все породы")
    def test_get_pets_breeds(self, pets_start):
        pets_start.get_pets_breeds()

    @pytest.mark.positive
    @allure.title("GET /api/v2/clients/{client_id}/pets/{pet_id} — питомец по ID")
    def test_get_pet_by_client(self, pets_start):
        pets_start.get_pet_by_client(client_id=1, pet_id=1)
