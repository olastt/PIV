import allure
from base.methods.calls.calls_methods import CallsMethods


class CallsStart:
    """Стартовые сценарии для Calls."""

    def __init__(self):
        self.calls = CallsMethods()

    def get_user_calls(self, user_id=1, page_number=1, page_size=20,
                       filter_status='save', clinic_id=1):
        params = {
            "page[number]": page_number,
            "page[size]": page_size,
            "filter[status]": filter_status, ### save, called, deleted
            "clinic_id": clinic_id,
        }
        with allure.step("Запрос прозвонов пользователя"):
            response = self.calls.get_user_calls(user_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_calls_search(self, user_id=1, page_number=1, page_size=20,
                       status='save', clinic_id=1):
        params = {
            "user_id":user_id,
            "page[number]": page_number,
            "page[size]": page_size,
            "status": status,  ### save, called, deleted
            "clinic_id": clinic_id,
        }
        with allure.step("Запрос поиска прозвонов"):
            response = self.calls.get_calls_search(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def create_user_call(self, user_id=1):
        json_data = {
            "call_data": {
                "date": "2026-03-13 14:00:00",
                "status": "save",
                "pet_id": 4,
                "note": "test postman",
                "clinic_id": 1,
            }
        }
        with allure.step("Создание прозвона"):
            response = self.calls.create_user_call(user_id, json_data=json_data)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def update_user_call(self, user_id=1, call_id=1, json_data=None):
        if json_data is None:
            json_data = {
                "call_data": {
                    "date": "2025-03-30 11:20:36",
                    "status": "called",
                    "pet_id": 4,
                    "note": "test postman5",
                    "clinic_id": 1,
                }
            }
        with allure.step("Обновление прозвона"):
            response = self.calls.update_user_call(user_id, call_id, json_data=json_data)
        with allure.step("Проверка статус кода 200 или 201"):
            response.assert_status_code([200, 201])
        return response

    def get_user_call_by_id(self, user_id=1, call_id=1, params=None):
        with allure.step("Запрос прозвона по ID"):
            response = self.calls.get_user_call_by_id(user_id, call_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
