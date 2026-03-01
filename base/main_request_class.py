import os
import httpx
from dotenv import load_dotenv
from base.attach_curl import attach_response_info
from base.response import Response
from settings import base_settings

load_dotenv()


class ApiClient:
    """
    Базовый класс для работы с API.
    Предоставляет общие методы для HTTP запросов и централизованное управление конфигурацией.
    """

    def __init__(self, base_url: str = None, api_key: str = None, default_headers: dict = None):
        """
        Инициализация базового клиента API.

        :param base_url: Базовый URL API. Если не указан, используется из base_settings
        :param api_key: API ключ. Если не указан, берется из переменных окружения
        :param default_headers: Заголовки по умолчанию. Если не указаны, используются стандартные
        """
        self.base_url = (base_url or base_settings.vm_url).rstrip('/')
        self.api_key = api_key or os.getenv("X_REST_API_KEY")
        self.errors = []

        # Базовые заголовки по умолчанию
        if default_headers is None:
            default_headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

        self.default_headers = default_headers.copy()

        # Добавляем API ключ, если он есть
        if self.api_key:
            self.default_headers["X-REST-API-KEY"] = self.api_key

    def _get_headers(self, headers: dict = None) -> dict:
        """
        Объединяет заголовки по умолчанию с переданными заголовками.

        :param headers: Дополнительные заголовки
        :return: Объединенные заголовки
        """
        merged_headers = self.default_headers.copy()
        if headers:
            merged_headers.update(headers)
        return merged_headers

    def _build_url(self, endpoint: str) -> str:
        """
        Строит полный URL из базового URL и endpoint.

        :param endpoint: Путь endpoint (может начинаться с / или без него)
        :return: Полный URL
        """
        endpoint = endpoint.strip('/')
        return f"{self.base_url}/{endpoint}" if endpoint else self.base_url

    def _handle_request_error(self, error: Exception, operation: str):
        """
        Обрабатывает ошибки при выполнении запросов.

        :param error: Исключение, которое произошло
        :param operation: Описание операции для логирования
        """
        error_msg = f"Ошибка при выполнении {operation}: {str(error)}"
        self.errors.append(error_msg)
        if isinstance(error, httpx.TimeoutException):
            raise Exception(f"Timeout occurred during {operation}")
        elif isinstance(error, httpx.RequestError):
            raise Exception(f"Request error during {operation}: {str(error)}")
        else:
            raise Exception(error_msg)

    def _send_request(
            self,
            method: str,
            url: str,
            headers: dict = None,
            params: dict = None,
            json_data: dict = None,
            data: dict = None,
            timeout: float = 90
    ) -> Response:
        """
        Универсальный метод для отправки HTTP запросов.

        :param method: HTTP метод (GET, POST, PUT, DELETE, PATCH)
        :param url: Полный URL запроса
        :param headers: Дополнительные заголовки
        :param params: Query параметры (для GET запросов)
        :param json_data: Данные для отправки в формате JSON
        :param data: Данные для отправки в формате form-data
        :param timeout: Таймаут запроса в секундах
        :return: Объект Response
        """
        merged_headers = self._get_headers(headers)
        method_upper = method.upper()
        operation = f"{method_upper} {url}"

        try:
            if method_upper == "GET":
                raw_response = httpx.get(url, headers=merged_headers, params=params, timeout=timeout)
            elif method_upper == "POST":
                raw_response = httpx.post(
                    url, headers=merged_headers, params=params, json=json_data, data=data, timeout=timeout
                )
            elif method_upper == "PUT":
                raw_response = httpx.put(
                    url, headers=merged_headers, params=params, json=json_data, data=data, timeout=timeout
                )
            elif method_upper == "PATCH":
                raw_response = httpx.patch(
                    url, headers=merged_headers, params=params, json=json_data, data=data, timeout=timeout
                )
            elif method_upper == "DELETE":
                raw_response = httpx.delete(url, headers=merged_headers, params=params, timeout=timeout)
            else:
                raise ValueError(f"Метод {method_upper} не поддерживается")

            attach_response_info(raw_response)
            return Response(raw_response)

        except Exception as e:
            self._handle_request_error(e, operation)

    def get(self, endpoint: str, headers: dict = None, params: dict = None, timeout: float = 90) -> Response:
        """Выполняет GET запрос"""
        url = self._build_url(endpoint)
        return self._send_request("GET", url, headers=headers, params=params, timeout=timeout)

    def post(
            self, endpoint: str, json_data: dict = None, data: dict = None,
            headers: dict = None, params: dict = None, timeout: float = 90
    ) -> Response:
        """Выполняет POST запрос"""
        url = self._build_url(endpoint)
        return self._send_request("POST", url, headers=headers, params=params, json_data=json_data, data=data,
                                  timeout=timeout)

    def put(
            self, endpoint: str, json_data: dict = None, data: dict = None,
            headers: dict = None, params: dict = None, timeout: float = 90
    ) -> Response:
        """Выполняет PUT запрос"""
        url = self._build_url(endpoint)
        return self._send_request("PUT", url, headers=headers, params=params, json_data=json_data, data=data,
                                  timeout=timeout)

    def patch(
            self, endpoint: str, json_data: dict = None, data: dict = None,
            headers: dict = None, params: dict = None, timeout: float = 90
    ) -> Response:
        """Выполняет PATCH запрос"""
        url = self._build_url(endpoint)
        return self._send_request("PATCH", url, headers=headers, params=params, json_data=json_data, data=data,
                                  timeout=timeout)

    def delete(self, endpoint: str, headers: dict = None, params: dict = None, timeout: float = 90) -> Response:
        """Выполняет DELETE запрос"""
        url = self._build_url(endpoint)
        return self._send_request("DELETE", url, headers=headers, params=params, timeout=timeout)

    def check_errors_during_test(self):
        """
        Проверяет наличие ошибок, накопленных во время выполнения теста.
        Вызывает исключение, если есть ошибки.
        """
        if self.errors:
            errors_copy = self.errors.copy()
            self.errors.clear()
            raise AssertionError(f"Во время выполнения теста возникли ошибки: {errors_copy}")
