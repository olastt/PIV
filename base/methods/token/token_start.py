import hashlib
import os

import allure
from dotenv import set_key

from base.methods.token.token_methods import TokenMethods
from base.piv_client import PivApiClient
from src.config.url import Url


def _get_project_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def _get_env_path():
    return os.path.join(_get_project_root(), ".env")


def compute_piv_api_key(token: str, domain: str) -> str:
    """Временный ключ коллекции для запроса /apiKey/byClinicCode (md5(token + domain))."""
    return hashlib.md5(f"{token}{domain}".encode()).hexdigest()


def _extract_token_from_response(response_json: dict) -> str:
    data = response_json.get("data")
    if isinstance(data, dict):
        return data.get("token") or data.get("user_token") or data.get("api_key")
    if isinstance(data, str):
        return data
    return response_json.get("token") or response_json.get("user_token")


def extract_clinic_api_key(response_json: dict) -> str:
    data = response_json.get("data")
    if isinstance(data, dict):
        api_key = data.get("apiKey")
        if api_key:
            return str(api_key)
    raise AssertionError(f"В ответе /apiKey/byClinicCode не найден data.apiKey: {response_json}")


def write_collection_key_to_env(collection_key: str, env_path: str = None):
    path = env_path or _get_env_path()
    set_key(path, "API_TOKEN_COLLECTION", collection_key)
    os.environ["API_TOKEN_COLLECTION"] = collection_key


def write_clinic_api_key_to_env(clinic_api_key: str, env_path: str = None):
    path = env_path or _get_env_path()
    set_key(path, "X_API_KEY", clinic_api_key)
    os.environ["X_API_KEY"] = clinic_api_key


def fetch_clinic_api_key(clinic_code: str, collection_key: str) -> str:
    client = PivApiClient(api_key=collection_key)
    response = client.get(Url.GET_API_KEY_BY_CLINIC_CODE, params={"code": clinic_code})
    response.assert_status_code(200)
    return extract_clinic_api_key(response.response_json or {})


class TokenStart:
    """getToken → md5 → /apiKey/byClinicCode → clinic apiKey для всех PIV-запросов."""

    def __init__(self):
        self.token = TokenMethods()

    def bootstrap_piv_session(
        self,
        login=None,
        password=None,
        app_name=None,
        domain=None,
        clinic_code=None,
        token_service=None,
    ):
        login = login or os.getenv("LOGIN_PIV") or os.getenv("LOGIN")
        password = password or os.getenv("PASSWORD_PIV") or os.getenv("PASSWORD")
        app_name = app_name or os.getenv("APP_NAME_PIV") or os.getenv("APP_NAME")
        domain = domain or os.getenv("DOMAIN_PIV") or os.getenv("DOMAIN")
        clinic_code = clinic_code or os.getenv("CLINIC_CODE", "10001")

        if not login or not password:
            raise AssertionError("Для PIV нужны LOGIN/LOGIN_PIV и PASSWORD/PASSWORD_PIV в .env")
        if not domain:
            raise AssertionError("Для PIV нужен DOMAIN_PIV или DOMAIN в .env")

        service = token_service or self.token
        auth_url = Url.DOMAIN_VM_AUTH.rstrip("/")

        with allure.step(f"POST getToken на {auth_url}{Url.AUTH_BY_LOGIN_AND_PASSWORD}"):
            response = service.get_token(login=login, password=password, app_name=app_name)

        with allure.step(f"Проверка: getToken ушёл на Vetmanager auth ({auth_url})"):
            request_url = str(getattr(response.response, "url", ""))
            assert auth_url in request_url, (
                f"getToken должен идти на {auth_url}, получен URL: {request_url}"
            )

        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)

        token = _extract_token_from_response(response.response_json or {})
        assert token, "В ответе getToken не найден data.token"

        collection_key = compute_piv_api_key(token, domain)
        with allure.step("Сохранение collection key (md5) для /apiKey/byClinicCode"):
            write_collection_key_to_env(collection_key)

        with allure.step(f"GET /apiKey/byClinicCode?code={clinic_code}"):
            clinic_api_key = fetch_clinic_api_key(clinic_code, collection_key)

        with allure.step("Сохранение clinic apiKey в X-API-KEY для всех PIV-запросов"):
            write_clinic_api_key_to_env(clinic_api_key)

        return response

    def get_token_and_save_api_key(self, **kwargs):
        return self.bootstrap_piv_session(**kwargs)
