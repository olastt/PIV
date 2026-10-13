import allure
import pytest
from Library.MakeyIS import Test

from tests.helpers.piv_positive import assert_collection_count, assert_piv_success


class TestMedicalcardsPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/recomendations")
    @allure.title("Получение рекомендаций клиента")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_recomendations(self, medicalcards_start):
        body = assert_piv_success(medicalcards_start.get_recomendations())
        assert_collection_count(body["data"], "recomendation")

    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/vaccinations")
    @allure.title("Получение вакцинаций клиента")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_vaccinations(self, medicalcards_start):
        body = assert_piv_success(medicalcards_start.get_vaccinations())
        assert_collection_count(body["data"], "vaccination")
