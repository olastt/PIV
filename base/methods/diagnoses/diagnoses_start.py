import allure
from base.methods.diagnoses.diagnoses_methods import DiagnosesMethods


class DiagnosesStart:
    """Стартовые сценарии для Diagnoses."""

    def __init__(self):
        self.diagnoses = DiagnosesMethods()

    def get_diagnoses(self, params=None):
        with allure.step("Запрос списка диагнозов"):
            response = self.diagnoses.get_diagnoses(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_diagnos_by_id(self, diagnos_id=1, params=None):
        with allure.step("Запрос диагноза по ID"):
            response = self.diagnoses.get_diagnos_by_id(diagnos_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response
