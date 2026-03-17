# Тесты авторизации VM: логин, получение токена, запись в .env
import os
import allure
import pytest
from dotenv import load_dotenv

# Подтягиваем .env из корня проекта (mobile-)
_load_env = load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"))


@allure.epic("API по Swagger")
@allure.feature("Auth")
class TestAuthPositive:

    @pytest.mark.positive
    @allure.title("Авторизация по логину и паролю, запись токена в .env")
    def test_auth_with_login_and_password_and_save_token(self, auth_start):
        """
        Логин в VM: при auth_with_login_and_password() без аргументов
        берутся LOGIN, PASSWORD, APP_NAME из .env.
        Можно передать явно: auth_with_login_and_password(login="...", password="...", app_name="...").
        """
        # Явно передаём из окружения (подгружается в conftest из mobile-/.env)
        auth_start.auth_with_login_and_password(
            login=os.getenv("LOGIN"),
            password=os.getenv("PASSWORD"),
            app_name=os.getenv("APP_NAME"),
        )
