import allure
from base.methods.diagnoses.diagnoses_methods import DiagnosesMethods


class DiagnosesStart:
    """Стартовые сценарии для Diagnoses."""

    def __init__(self):
        self.diagnoses = DiagnosesMethods()

    def get_diagnoses(self):
        with allure.step("Запрос списка диагнозов"):
            response = self.diagnoses.get_diagnoses()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_diagnos_by_id(self, diagnos_id=1, params=None):
        with allure.step("Запрос диагноза по ID"):
            response = self.diagnoses.get_diagnos_by_id(diagnos_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def create_diagnos(self, json_data=None):
        if json_data is None:
            json_data = {
                "diagnos_data": {
                    "title": "Testik",
                    "status": "ACTIVE",
                }
            }
        with allure.step("Создание диагноза"):
            response = self.diagnoses.post_diagnos(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response

    def update_diagnos(self, diagnos_id=133, json_data=None):
        if json_data is None:
            json_data = {
                "diagnos_data": {
                    "title": "Test diagnos",
                    "status": "ACTIVE",
                }
            }
        with allure.step("Обновление диагноза"):
            response = self.diagnoses.patch_diagnos(diagnos_id, json_data)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def delete_diagnos(self, diagnos_id=1):
        with allure.step("Удаление диагноза"):
            response = self.diagnoses.delete_diagnos(diagnos_id)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response
