import allure
import pytest
from Library.MakeyIS import Test

from base.piv_client import PivApiClient
from src.config.url import Url
from src.schemas.piv.errors import PivErrorResponse
from tests.helpers.piv_negative import INVALID_API_KEY, assert_piv_error


class TestEventsNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("POST /event")
    @allure.title("400 — отсутствует обязательный параметр device_id")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_missing_device_id_returns_400(self):
        response = PivApiClient().post(Url.POST_EVENT, json_data={})
        assert_piv_error(response, 400, PivErrorResponse)
        assert "device_id" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("POST /event")
    @allure.title("400 — отсутствует обязательный параметр title")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_missing_title_returns_400(self):
        response = PivApiClient().post(Url.POST_EVENT, json_data={"device_id": 1})
        assert_piv_error(response, 400, PivErrorResponse)
        assert "title" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("POST /event")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).post(
            Url.POST_EVENT,
            json_data={"device_id": 1, "title": "Визиты"},
        )
        assert_piv_error(response, 403, PivErrorResponse)
