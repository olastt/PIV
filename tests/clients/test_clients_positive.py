import allure
import pytest
from Library.MakeyIS import Test


class TestClientsPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /clients/clientByPhone")
    @allure.title("Проверка клиента по номеру телефона")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_client_by_phone(self, clients_start):
        clients_start.get_client_by_phone("9184140259")
