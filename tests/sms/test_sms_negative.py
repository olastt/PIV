import allure
import pytest
from Library.MakeyIS import Test

from base.piv_client import PivApiClient
from src.config.url import Url
from src.schemas.piv.errors import PivErrorResponse, PivSmsCheckErrorResponse
from tests.helpers.piv_negative import INVALID_API_KEY, assert_piv_error


class TestSmsNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("POST /sms/send")
    @allure.title("400 — отсутствует обязательный параметр phone")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_send_sms_missing_phone_returns_400(self):
        response = PivApiClient().post(Url.POST_SEND_SMS, json_data={})
        assert_piv_error(response, 400, PivErrorResponse)
        assert "phone" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("POST /sms/send")
    @allure.title("403 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_send_sms_invalid_api_key_returns_403(self):
        response = PivApiClient(api_key=INVALID_API_KEY).post(
            Url.POST_SEND_SMS,
            json_data={"phone": "79184140259"},
        )
        assert_piv_error(response, 403, PivErrorResponse)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /sms/check")
    @allure.title("400 — отсутствует обязательный параметр phone")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_check_sms_missing_phone_returns_400(self):
        response = PivApiClient().get(Url.GET_SMS_CHECK)
        assert_piv_error(response, 400, PivErrorResponse)
        assert "phone" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /sms/check")
    @allure.title("400 — отсутствует обязательный параметр code")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_check_sms_missing_code_returns_400(self):
        response = PivApiClient().get(
            Url.GET_SMS_CHECK,
            params={"phone": "79184140259"},
        )
        assert_piv_error(response, 400, PivErrorResponse)
        assert "code" in response.response_json[0]["message"].lower()

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /sms/check")
    @allure.title("500 — номер телефона не найден")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_check_sms_phone_not_found_returns_500(self):
        response = PivApiClient().get(
            Url.GET_SMS_CHECK,
            params={"phone": "0000000000", "code": "1234"},
        )
        assert_piv_error(response, 500, PivSmsCheckErrorResponse)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /sms/check")
    @allure.title("500 — неверный код из SMS")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_check_sms_invalid_code_returns_500(self):
        response = PivApiClient().get(
            Url.GET_SMS_CHECK,
            params={"phone": "79184140259", "code": "0000"},
        )
        assert_piv_error(response, 500, PivSmsCheckErrorResponse)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("GET /sms/check")
    @allure.title("500 — некорректный X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_check_sms_invalid_api_key_returns_500(self):
        response = PivApiClient(api_key=INVALID_API_KEY).get(
            Url.GET_SMS_CHECK,
            params={"phone": "79184140259", "code": "1234"},
        )
        assert_piv_error(response, 500, PivSmsCheckErrorResponse)
