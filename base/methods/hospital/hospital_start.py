import allure
from base.methods.hospital.hospital_methods import HospitalMethods


class HospitalStart:
    """Стартовые сценарии для Hospital."""

    def __init__(self):
        self.hospital = HospitalMethods()

    def get_hospital(self, page_size=20, page_number=1,
                     sort_direction="asc", filter_status='in_hospital'):
        params = {
            "page[size]": page_size,
            "page[number]": page_number,
            "sort[direction]": sort_direction,
            "filter[status]": filter_status ### in_hospital, planned, delayed, discharged
        }
        with allure.step("Запрос данных стационара"):
            response = self.hospital.get_hospital(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_hospital_blocks(self, params=None):
        with allure.step("Запрос блоков стационара"):
            response = self.hospital.get_hospital_blocks(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_hospital_list_statuses(self, params=None):
        with allure.step("Запрос статусов стационара"):
            response = self.hospital.get_hospital_list_statuses(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_hospital_by_id(self, record_id=2, params=None):
        with allure.step("Запрос записи стационара по ID"):
            response = self.hospital.get_hospital_by_id(record_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def update_hospital_by_record_id(self, record_id=1, json_data=None):
        if json_data is None:
            json_data = {
                "hospital_data": {
                    "start_date": "2026-03-20 14:39:23",
                    "end_date": "2026-03-25 07:20:00",
                    "client_id": 623,
                    "pet_id": 51,
                    "user_id": 10,
                    "place": "1",
                    "hospital_block_id": 2,
                    "description": "какое-то описание Тестовое из постман22222",
                    "status": "planned",
                }
            }
        with allure.step("Обновление записи стационара (UpdateHospitalByRecordId)"):
            response = self.hospital.patch_hospital_by_id(record_id, json_data)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
