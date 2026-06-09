import allure
import pytest
from Library.MakeyIS import Test


class TestClientsPositive:
    @pytest.mark.positive
    @allure.epic("Клиенты")
    @allure.feature("GET /api/v2/clients/{client_id}")
    @allure.title("Получение информации о клиенте")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_get_client_by_id(self, clients_start):
        clients_start.get_client_by_id()

    @pytest.mark.positive
    @allure.epic("Клиенты")
    @allure.feature("GET /api/v2/clients/search/")
    @allure.title("Поиск по базе клиентов")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_get_clients_search(self, clients_start):
        clients_start.get_clients_search()

    @pytest.mark.positive
    @allure.epic("Клиенты")
    @allure.feature("GET /api/v2/clients/{client_id}/pets")
    @allure.title("Получение питомцев клиента")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_get_client_pets(self, clients_start):
        clients_start.get_client_pets()

    @pytest.mark.positive
    @allure.epic("Клиенты")
    @allure.feature("GET /api/v2/clients/{client_id}/match")
    @allure.title("Сопоставление клиента")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_clients_match(self, clients_start):
        clients_start.get_client_match()

    @pytest.mark.positive
    @allure.epic("Клиенты")
    @allure.feature("GET /api/v2/clients/{client_id}/contacts")
    @allure.title("Получение контактов клиента")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_contacts_info_by_client(self, clients_start):
        clients_start.get_client_contacts()

    @pytest.mark.positive
    @allure.epic("Клиенты")
    @allure.feature("GET /api/v2/clients/{client_id}/pets/{pet_id}")
    @allure.title("Получение питомца клиента по ID")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_pet_info_by_client(self, clients_start):
        clients_start.get_client_pet_by_id()

    @pytest.mark.positive
    @allure.epic("Клиенты")
    @allure.feature("PATCH /api/v2/clients/{client_id}")
    @allure.title("Обновление клиента")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_patch_client(self, clients_start):
        clients_start.patch_client(client_id=1)

    @pytest.mark.positive
    @allure.epic("Клиенты")
    @allure.feature("POST /api/v2/clients")
    @allure.title("Создание клиента")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_create_client(self, clients_start):
        clients_start.post_client()
