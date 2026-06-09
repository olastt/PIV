import allure
import pytest
from Library.MakeyIS import Test

class TestPetsPositive:

    @pytest.mark.positive
    @allure.epic("Питомцы")
    @allure.feature("GET /api/v2/pets/types")
    @allure.title('Получение типов питомцев')
    @Test(run_test=True, group_name="Питомцы", log=True)
    def test_get_pets_types(self, pets_start):
        pets_start.get_pets_types()

    @pytest.mark.positive
    @allure.epic("Питомцы")
    @allure.feature("GET /api/v2/pets/genders")
    @allure.title('Получение пола питомцев')
    @Test(run_test=True, group_name="Питомцы", log=True)
    def test_get_pets_genders(self, pets_start):
        pets_start.get_pets_genders()

    @pytest.mark.positive
    @allure.epic("Питомцы")
    @allure.feature("GET /api/v2/pets/types/{type_id}/breeds")
    @allure.title('Получение породы по типу')
    @Test(run_test=True, group_name="Питомцы", log=True)
    def test_get_breeds_by_type(self, pets_start):
        pets_start.get_breeds_by_type(type_id=1)

    @pytest.mark.positive
    @allure.epic("Питомцы")
    @allure.feature("GET /api/v2/pets/breeds")
    @allure.title('Получение всех типов пород')
    @Test(run_test=True, group_name="Питомцы", log=True)
    def test_get_pets_breeds(self, pets_start):
        pets_start.get_pets_breeds()

    @pytest.mark.positive
    @allure.epic("Питомцы")
    @allure.feature("GET /api/v2/clients/{client_id}/pets/{pet_id}")
    @allure.title('Получение питомца по ID')
    @Test(run_test=True, group_name="Питомцы", log=True)
    def test_get_pet_by_client(self, pets_start):
        pets_start.get_pet_by_client(client_id=1, pet_id=1)

    @pytest.mark.positive
    @allure.epic("Питомцы")
    @allure.feature("POST /api/v2/clients/{client_id}/pets")
    @allure.title('Создание питомца')
    @Test(run_test=True, group_name="Питомцы", log=True)
    def test_post_client_pet(self, pets_start):
        pets_start.post_client_pet(client_id=1)

    @pytest.mark.positive
    @allure.epic("Питомцы")
    @allure.feature("PATCH /api/v2/clients/{client_id}/pets/{pet_id}")
    @allure.title('Обновление питомца')
    @Test(run_test=True, group_name="Питомцы", log=True)
    def test_patch_client_pet(self, pets_start):
        pets_start.patch_client_pet(client_id=1, pet_id=1)
