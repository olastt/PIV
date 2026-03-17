import allure
from base.methods.hospital.hospital_methods import HospitalMethods


class HospitalStart:
    """Стартовые сценарии для Hospital."""

    def __init__(self):
        self.hospital = HospitalMethods()

    def get_hospital(self, params=None):
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

    def get_hospital_by_id(self, record_id=1, params=None):
        with allure.step("Запрос записи стационара по ID"):
            response = self.hospital.get_hospital_by_id(record_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
