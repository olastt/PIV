import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_piv_success


class TestClientsPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /clients/clientByPhone")
    @allure.title("Проверка клиента по номеру телефона")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_client_by_phone(self, clients_start):
        body = assert_piv_success(clients_start.get_client_by_phone())
        assert body["data"]["client_id"] > 0, "client_id должен быть положительным"
