import os

import allure
import pytest
from dotenv import load_dotenv
from Library.MakeyIS import Test

from src.config.url import Url
from tests.helpers.piv_positive import assert_json_body, assert_nonempty_string


load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"))


class TestTokenPositive:
    @pytest.mark.positive
    @allure.epic("PIV")
    @allure.feature("POST getToken")
    @allure.title("Получение token с Vetmanager и формирование X-API-KEY")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_get_token_and_save_api_key(self, token_start):
        response = token_start.get_token_and_save_api_key(
            login=os.getenv("LOGIN_PIV") or os.getenv("LOGIN"),
            password=os.getenv("PASSWORD_PIV") or os.getenv("PASSWORD"),
            app_name=os.getenv("APP_NAME_PIV") or os.getenv("APP_NAME"),
        )
        auth_url = Url.DOMAIN_VM_AUTH.rstrip("/")
        assert auth_url in str(response.response.url)
        body = assert_json_body(response)
        assert body["status"] == 200, "status в теле должен подтверждать успешную авторизацию"
        assert_nonempty_string(body["data"]["token"], "data.token")
        assert_nonempty_string(body["data"]["user_id"], "data.user_id")
