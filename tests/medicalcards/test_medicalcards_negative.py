import allure
import pytest
from Library.MakeyIS import Test

from base.piv_client import PivApiClient
from src.config.url import Url
from src.schemas.piv.errors import PivErrorResponse, PivServerErrorMessageResponse
from tests.helpers.piv_negative import INVALID_API_KEY, assert_piv_error


class TestMedicalcardsNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/recomendations")
    @allure.title("400 — отсутствует обязательный параметр client_id")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_recomendations_missing_client_id_returns_400(self):
        response = PivApiClient().get(Url.GET_RECOMENDATIONS_BY_CLIENT_ID)
        assert_piv_error(response, 400, PivErrorResponse)
        assert "client_id" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/recomendations")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_recomendations_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).get(
            Url.GET_RECOMENDATIONS_BY_CLIENT_ID,
            params={"client_id": 6},
        )
        assert_piv_error(response, 403, PivErrorResponse)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/recomendations")
    @allure.title("500 — client_id не найден")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_recomendations_invalid_client_id_returns_500(self):
        response = PivApiClient().get(
            Url.GET_RECOMENDATIONS_BY_CLIENT_ID,
            params={"client_id": 999999999},
        )
        assert_piv_error(response, 500, PivServerErrorMessageResponse)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/vaccinations")
    @allure.title("400 — отсутствует обязательный параметр client_id")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_vaccinations_missing_client_id_returns_400(self):
        response = PivApiClient().get(Url.GET_VACCINATIONS_BY_CLIENT_ID)
        assert_piv_error(response, 400, PivErrorResponse)
        assert "client_id" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /medicalCards/vaccinations")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_vaccinations_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).get(
            Url.GET_VACCINATIONS_BY_CLIENT_ID,
            params={"client_id": 6},
        )
        assert_piv_error(response, 403, PivErrorResponse)
