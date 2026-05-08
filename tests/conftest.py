"""
Корневой conftest: фикстуры auth_start и common_start доступны всем тестам,
чтобы тесты в tests/auth/ и при любом способе запуска находили их.
"""
import os
import pytest
from dotenv import load_dotenv

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_project_root, ".env"))

from base.methods.auth.auth_start import AuthStart
from base.methods.common.common_start import CommonStart


@pytest.fixture
def auth_start():
    return AuthStart()


@pytest.fixture(scope="session", autouse=True)
def ensure_auth_token():
    """
    Гарантирует наличие токена перед запуском API-тестов.
    При наличии LOGIN/PASSWORD всегда обновляет токен в начале сессии,
    чтобы избежать 401 из-за протухшего токена в .env.
    """
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    app_name = os.getenv("APP_NAME")
    domain = os.getenv("DOMAIN")
    clinic_id = os.getenv("CLINIC_ID")

    # Большинство mobile API endpoint требуют DOMAIN; без него сервер вернет 401.
    if not domain:
        raise AssertionError(
            "В .env отсутствует DOMAIN. Добавьте DOMAIN=<имя_домена_клиники>, "
            "иначе API будет возвращать 401 (No domain name found)."
        )

    if not clinic_id:
        raise AssertionError(
            "В .env отсутствует CLINIC_ID. Добавьте CLINIC_ID=<id_клиники>, "
            "иначе API будет возвращать 401 (No clinic id found)."
        )

    # Для совместимости заголовка X-MOBILE-APP подставляем APP_NAME, если нужно.
    if app_name and not os.getenv("X_MOBILE_APP"):
        os.environ["X_MOBILE_APP"] = app_name

    if login and password:
        AuthStart.auth_with_login_and_password(login=login, password=password, app_name=app_name)
        return

    token = os.getenv("X_REST_API_KEY") or os.getenv("X_TOKEN") or os.getenv("TOKEN")
    if not token:
        raise AssertionError(
            "Для запуска API-тестов нужны LOGIN/PASSWORD (для получения токена) "
            "или уже установленный X_REST_API_KEY/X_TOKEN/TOKEN."
        )


@pytest.fixture
def common_start():
    start = CommonStart()
    yield start
