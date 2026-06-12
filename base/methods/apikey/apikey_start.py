import os

import allure

from base.methods.apikey.apikey_methods import ApikeyMethods
from base.methods.token.token_start import extract_clinic_api_key, write_clinic_api_key_to_env


class ApikeyStart:
    def __init__(self):
        self.apikey = ApikeyMethods()

    def get_api_key_by_clinic_code(self, code=None):
        code = code or os.getenv("CLINIC_CODE", "10077")
        with allure.step("GET /apiKey/byClinicCode"):
            response = self.apikey.get_api_key_by_clinic_code(code)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        with allure.step("Сохранение clinic apiKey из ответа в X-API-KEY"):
            clinic_api_key = extract_clinic_api_key(response.response_json or {})
            write_clinic_api_key_to_env(clinic_api_key)
        return response
