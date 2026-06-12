import allure
import pytest
from Library.MakeyIS import Test


class TestMedicalcardsPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/recomendations")
    @allure.title("Получение рекомендаций клиента")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_recomendations(self, medicalcards_start):
        medicalcards_start.get_recomendations()

    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/vaccinations")
    @allure.title("Получение вакцинаций клиента")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_vaccinations(self, medicalcards_start):
        medicalcards_start.get_vaccinations()
