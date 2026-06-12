import os

import httpx
from dotenv import load_dotenv

from base.attach_curl import attach_response_info
from base.response import Response

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_project_root, ".env"))


class ApiClient:
    """Базовый HTTP-клиент: GET/POST, Allure, обёртка Response."""

    def __init__(self, base_url: str, default_headers: dict = None):
        if not base_url:
            raise ValueError("base_url обязателен")
        self.base_url = base_url.rstrip("/")
        self.default_headers = (default_headers or {
            "accept": "application/json",
            "Content-Type": "application/json",
        }).copy()

    def _get_headers(self, headers: dict = None) -> dict:
        merged = self.default_headers.copy()
        if headers:
            merged.update(headers)
        return merged

    def _build_url(self, endpoint: str) -> str:
        endpoint = endpoint.strip("/")
        return f"{self.base_url}/{endpoint}" if endpoint else self.base_url

    def _send_request(
        self,
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        json_data: dict = None,
        data: dict = None,
        timeout: float = 90,
    ) -> Response:
        merged_headers = self._get_headers(headers)
        method_upper = method.upper()

        try:
            if method_upper == "GET":
                raw_response = httpx.get(
                    url, headers=merged_headers, params=params, timeout=timeout
                )
            elif method_upper == "POST":
                raw_response = httpx.post(
                    url,
                    headers=merged_headers,
                    params=params,
                    json=json_data,
                    data=data,
                    timeout=timeout,
                )
            else:
                raise ValueError(f"Метод {method_upper} не поддерживается")

            attach_response_info(raw_response)
            return Response(raw_response)

        except httpx.TimeoutException as exc:
            raise TimeoutError(f"Timeout: {method_upper} {url}") from exc
        except httpx.RequestError as exc:
            raise ConnectionError(f"Request error: {method_upper} {url}: {exc}") from exc

    def get(
        self,
        endpoint: str,
        headers: dict = None,
        params: dict = None,
        timeout: float = 90,
    ) -> Response:
        return self._send_request(
            "GET", self._build_url(endpoint), headers=headers, params=params, timeout=timeout
        )

    def post(
        self,
        endpoint: str,
        json_data: dict = None,
        data: dict = None,
        headers: dict = None,
        params: dict = None,
        timeout: float = 90,
    ) -> Response:
        return self._send_request(
            "POST",
            self._build_url(endpoint),
            headers=headers,
            params=params,
            json_data=json_data,
            data=data,
            timeout=timeout,
        )
