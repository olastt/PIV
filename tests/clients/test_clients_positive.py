# Тесты по Swagger: Clients
import allure
import pytest
from Library.MakeyIS import Test

class TestClientsPositive:

    @pytest.mark.positive
    @allure.epic('Клиенты')
    @allure.feature('GET /api/v2/clients/{client_id}')
    @allure.title('Получение информации о клиенте')
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_get_client_by_id(self, clients_start):
        clients_start.get_client_by_id(client_id=1)

    @pytest.mark.positive
    @allure.epic('Клиенты')
    @allure.feature('GET /api/v2/clients/search/')
    @allure.title("Поиск по базе клиентов")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_get_clients_search(self, clients_start):
        clients_start.get_clients_search(search_query="тест", page_number=1, page_size=20)

    @pytest.mark.positive
    @allure.epic('Клиенты')
    @allure.feature('GET /api/v2/clients/{client_id}/pets')
    @allure.title("Получение информации о питомцах клиента")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_get_client_pets(self, clients_start):
        clients_start.get_client_pets(client_id=1)

    @pytest.mark.positive
    @allure.epic('Клиенты')
    @allure.feature('GET /api/v2/clients/{client_id}/invoices')
    @allure.title("Получение информации о счетах клиента")
    @Test(run_test=True, group_name="Клиенты", log=True)
    def test_get_client_invoices(self, clients_start):
        clients_start.get_client_invoices(client_id=1)
