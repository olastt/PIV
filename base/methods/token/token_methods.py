import allure

from base.main_request_class import ApiClient
from src.config.url import Url


class TokenMethods(ApiClient):
    """POST getToken — только Vetmanager auth (devolesya.vetmanager2.ru)."""

    def __init__(self):
        super().__init__(
            base_url=Url.DOMAIN_VM_AUTH.rstrip("/"),
            default_headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "accept": "application/json",
            },
        )

    @allure.step("POST /token_auth.php — getToken (Vetmanager auth)")
    def get_token(self, login: str, password: str, app_name: str = None):
        data = {"login": login, "password": password}
        if app_name:
            data["app_name"] = app_name
        return self.post(Url.AUTH_BY_LOGIN_AND_PASSWORD, data=data, timeout=30)

    @property
    def auth_base_url(self) -> str:
        return Url.DOMAIN_VM_AUTH.rstrip("/")
