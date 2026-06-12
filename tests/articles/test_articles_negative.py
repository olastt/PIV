import allure
import pytest
from Library.MakeyIS import Test

from base.piv_client import PivApiClient
from src.config.url import Url
from src.schemas.piv.errors import PivErrorResponse, PivValidation422Response
from tests.helpers.piv_negative import INVALID_API_KEY, assert_piv_error


class TestArticlesNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /articles/lastThree")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_last_three_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).get(Url.GET_LAST_THREE_ARTICLES)
        assert_piv_error(response, 403, PivErrorResponse)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /articles")
    @allure.title("422 — отсутствуют обязательные параметры page и size")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_articles_missing_pagination_returns_422(self):
        response = PivApiClient().get(Url.GET_ARTICLES)
        assert_piv_error(response, 422, PivValidation422Response)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /articles")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_articles_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).get(
            Url.GET_ARTICLES,
            params={"page": 1, "size": 10},
        )
        assert_piv_error(response, 403, PivErrorResponse)
