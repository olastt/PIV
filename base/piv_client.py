import os

from base.main_request_class import ApiClient
from src.config.url import Url


class PivApiClient(ApiClient):
    """HTTP-клиент PIV — petinvet.ru/api/v2, заголовок X-API-KEY."""

    def __init__(self, api_key: str = None, base_url: str = None, default_headers: dict = None):
        if default_headers is None:
            default_headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

        resolved_api_key = api_key if api_key is not None else os.getenv("X_API_KEY")
        super().__init__(
            base_url=base_url or os.getenv("BASE_URL_PIV") or Url.DOMAIN_PET_PROD,
            default_headers=default_headers,
        )

        if resolved_api_key:
            self.default_headers["X-API-KEY"] = resolved_api_key
