import os

import allure
import pytest
from dotenv import load_dotenv
from Library.MakeyIS import Test


load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"))


class TestAuthPositive:
    @pytest.mark.positive
    @allure.epic("Логин")
    @allure.feature("POST /token_auth.php")
    @allure.title("Авторизация по логину и паролю, запись токена в .env")
    @Test(run_test=True, group_name="Логин", log=True)
    def test_auth_with_login_and_password_and_save_token(self, auth_start):
        auth_start.auth_with_login_and_password(
            login=os.getenv("LOGIN"),
            password=os.getenv("PASSWORD"),
            app_name=os.getenv("APP_NAME"),
        )
