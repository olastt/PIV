import allure
from base.main_request_class import ApiClient
from src.config.url import Url


class AuthMethods(ApiClient):
    """
    Методы авторизации в VetManager.
    Запрос на логин идёт на DOMAIN_VM_AUTH (devolesya.vetmanager2.ru).
    Токен из ответа сохраняется в .env и подставляется в остальные запросы к mobilebackend.
    """

    def __init__(self, api_key: str = None):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json",
        }
        # Логин только на хост авторизации; остальные методы ApiClient используют vm_url (mobilebackend)
        super().__init__(
            base_url=Url.DOMAIN_VM_AUTH,
            api_key=api_key,
            default_headers=headers,
        )

    @allure.step("POST /token_auth.php — авторизация по логину и паролю")
    def authorize(self, login: str = None, password: str = None, app_name: str = None):
        """
        Авторизация в VM.
        - Если параметр не передан (None) — из .env: LOGIN, PASSWORD, APP_NAME или X_MOBILE_APP (для app_name).
        """
        import os
        data = {}
        _login = login if login is not None else os.getenv("LOGIN")
        _password = password if password is not None else os.getenv("PASSWORD")
        _app_name = app_name if app_name is not None else os.getenv("APP_NAME") or os.getenv("X_MOBILE_APP")
        if _login:
            data["login"] = _login
        if _password:
            data["password"] = _password
        if _app_name:
            data["app_name"] = _app_name
        return self.post(Url.AUTH_BY_LOGIN_AND_PASSWORD, data=data, timeout=30)
