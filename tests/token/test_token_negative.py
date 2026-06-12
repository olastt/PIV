import allure
import pytest
from Library.MakeyIS import Test

from base.methods.token.token_methods import TokenMethods
from src.schemas.piv.errors import TokenUnauthorizedResponse
from tests.helpers.piv_negative import assert_piv_error


class TestTokenNegative:
    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("POST getToken")
    @allure.title("401 — неверные учётные данные")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_invalid_credentials_returns_401(self):
        response = TokenMethods().get_token(
            login="invalid_login",
            password="invalid_password",
            app_name="piv",
        )
        assert_piv_error(response, 401, TokenUnauthorizedResponse)

    @pytest.mark.negative
    @allure.epic("PIV")
    @allure.feature("POST getToken")
    @allure.title("401 — отсутствует app_name")
    @Test(run_test=True, group_name="PIV", log=True)
    def test_missing_app_name_returns_401(self):
        response = TokenMethods().get_token(login="admin", password="123456qq")
        assert_piv_error(response, 401, TokenUnauthorizedResponse)
