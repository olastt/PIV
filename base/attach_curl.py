import allure
import json
from curlify2 import Curlify


def attach_response_info(response):
    curl = Curlify(response.request)
    allure.attach(curl.to_curl(), name="cURL команда", attachment_type=allure.attachment_type.TEXT)

    if response.text:
        try:
            # Пытаемся парсить JSON и сделать его читаемым
            response_json = response.json()
            readable_json = json.dumps(response_json, indent=2, ensure_ascii=False)
            allure.attach(readable_json, name="Тело ответа", attachment_type=allure.attachment_type.JSON)
        except ValueError:
            # Если не JSON, прикрепляем как есть
            allure.attach(response.text, name="Тело ответа", attachment_type=allure.attachment_type.TEXT)