import json
import os
import allure
from dotenv import set_key

from base.methods.auth.auth_methods import AuthMethods


def _get_project_root():
    """Корень проекта (где лежит .env)."""
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def _get_env_path():
    return os.path.join(_get_project_root(), ".env")


def _extract_token_from_response(response_json: dict) -> str:
    """
    Извлекает токен из тела ответа авторизации.
    Поддерживает форматы: data.token, data.user_token, data как строка.
    """
    data = response_json.get("data")
    if isinstance(data, dict):
        return (
            data.get("token")
            or data.get("user_token")
            or data.get("api_key")
            or data.get("X-TOKEN")
        )
    if isinstance(data, str):
        return data
    # токен может быть в корне
    return (
        response_json.get("token")
        or response_json.get("user_token")
        or response_json.get("api_key")
    )


def write_token_to_env(token: str, env_path: str = None):
    """Записывает токен в .env (X_REST_API_KEY и X_TOKEN для совместимости)."""
    path = env_path or _get_env_path()
    set_key(path, "X_REST_API_KEY", token)
    set_key(path, "X_TOKEN", token)


class AuthStart:
    """Класс с методами для тестов авторизации и сохранения токена в .env."""

    @staticmethod
    def auth_with_login_and_password(auth_service=None, login=None, password=None, app_name=None):
        """
        Авторизация с логином и паролем.
        Если login/password/app_name не переданы — берутся из .env (LOGIN, PASSWORD, APP_NAME).
        При успехе извлекает токен из ответа и записывает в .env (X_REST_API_KEY, X_TOKEN).
        """
        _login = login if login is not None else os.getenv("LOGIN")
        _password = password if password is not None else os.getenv("PASSWORD")
        if not _login or not _password:
            raise AssertionError(
                "Для авторизации нужны LOGIN и PASSWORD. Задайте их в .env (в корне проекта mobile-) или передайте в вызов."
            )
        # Проверка: в Allure видно, что логин/пароль подставлены (при 401 убедитесь, что это нужные данные)
        allure.attach(
            f"LOGIN подставлен (длина {len(_login)}), PASSWORD подставлен (длина {len(_password)}). "
            "Файл .env должен быть в корне проекта mobile-.",
            "Credentials check",
            allure.attachment_type.TEXT,
        )
        service = auth_service or AuthMethods()
        response_data = service.authorize(login=login, password=password, app_name=app_name)

        with allure.step("Проверка статус кода 200"):
            if response_data.response_status != 200:
                url = getattr(response_data.response, "url", "?")
                body = response_data.response_json if response_data.response_json is not None else response_data.response.text
                body_str = json.dumps(body, ensure_ascii=False) if isinstance(body, dict) else str(body)
                allure.attach(body_str, "Response body", allure.attachment_type.JSON)
                raise AssertionError(
                    f"Ожидался 200, получен {response_data.response_status}. URL: {url}. Тело: {body}"
                )
            response_data.assert_status_code(200)

        with allure.step("Проверка на наличие данных"):
            data = response_data.response_json.get("data")
            assert data is not None, "В ответе не пришло данных (data)"

        with allure.step("Проверка тайтла успешной авторизации"):
            title = response_data.response_json.get("title")
            assert title == "Authorization completed.", (
                f"Ожидалось 'Authorization completed.', получено: {title!r}"
            )

        token = _extract_token_from_response(response_data.response_json or {})
        assert token, "В ответе не найден токен (data.token / data.user_token / data как строка)"

        with allure.step("Запись токена в .env"):
            write_token_to_env(token)

        return response_data
