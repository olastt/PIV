import os

import os

import allure
from dotenv import load_dotenv
from base.methods.users.users_methods import UserMethods

load_dotenv()


class UserStart:
    def __init__(self):
        self.users = UserMethods()

    def get_user_by_id(self, user_id: int = 1):
        with allure.step("Отправка запроса GET /api/v2/users/{user_id}"):
            response = self.users.get_user_by_id(user_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_user_home(self, user_id: int = 1, clinic_id: str = None):
        params = {"clinic_id": clinic_id} if clinic_id else None
        with allure.step("Запрос данных домашней страницы"):
            response = self.users.get_user_home(user_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_user_stores(self, user_id: int = 1):
        with allure.step("Запрос складов пользователя"):
            response = self.users.get_user_stores(user_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_user_schedules(self, user_id: int = 1, clinic_id: int = None, page_number=1, page_size=1):
        clinic_id = clinic_id or int(os.getenv("CLINIC_ID", "1"))
        params = {"page[number]": page_number, "page[size]": page_size, "clinic_id": clinic_id}
        with allure.step("GET /api/v2/users/{user_id}/schedules"):
            response = self.users.get_user_schedules(user_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_user_settings_payment(self, user_id: int = 1):
        with allure.step("GET /api/v2/users/{user_id}/settings/payment"):
            response = self.users.get_user_settings_payment(user_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_user_allowed_clinics(self, user_id: int = 1):
        with allure.step("GET /api/v2/users/{user_id}/allowedclinics"):
            response = self.users.get_user_allowed_clinics(user_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def patch_user(self, user_id: int = 1, json_data: dict = None):
        if json_data is None:
            json_data = {"user_data": {"nickname": f"pytest_{os.getenv('USER_ID', '1')}"}}
        with allure.step("PATCH /api/v2/users/{user_id}"):
            response = self.users.patch_user(user_id, json_data=json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        return response

    def post_user_logout(self, user_id: int = 1, json_data: dict = None):
        domain = os.getenv("DOMAIN", "test")
        if json_data is None:
            json_data = {
                "logout_data": {
                    "device_id": "pytest-device",
                    "clinic_id": str(os.getenv("CLINIC_ID", "1")),
                    "user_id": str(user_id),
                    "domain_name": domain,
                }
            }
        with allure.step("POST /api/v2/users/{user_id}/logout"):
            response = self.users.post_user_logout(user_id, json_data=json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 204, 401, 422])
        return response

    def patch_user_settings_payment(self, record_id: int = 0, json_data: dict = None):
        if json_data is None:
            json_data = {
                "settings_payment": {
                    "clinic_id": str(os.getenv("CLINIC_ID", "1")),
                    "cassa_id": str(os.getenv("CASSA_ID", "1")),
                    "user_id": str(os.getenv("USER_ID", "1")),
                }
            }
        with allure.step("PATCH /api/v2/users/settings/payment/{record_id}"):
            response = self.users.patch_user_settings_payment(record_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        return response

    def post_user_settings_payment_create(self, json_data: dict = None):
        if json_data is None:
            json_data = {
                "settings_payment": {
                    "clinic_id": str(os.getenv("CLINIC_ID", "1")),
                    "cassa_id": str(os.getenv("CASSA_ID", "1")),
                    "user_id": str(os.getenv("USER_ID", "1")),
                }
            }
        with allure.step("POST /api/v2/users/settings/payment/0"):
            response = self.users.post_user_settings_payment_create(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        return response

    def get_doctors(self, allow_limited: str = "0"):
        params = {"allow_limited": allow_limited}
        with allure.step("Запрос списка врачей"):
            response = self.users.get_doctors(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response