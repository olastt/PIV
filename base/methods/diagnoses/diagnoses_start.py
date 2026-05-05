import allure
from base.methods.diagnoses.diagnoses_methods import DiagnosesMethods


def _get_id_from_response(response):
    if not response or not getattr(response, "response_json", None):
        return None

    response_json = response.response_json
    data = response_json.get("data")
    if isinstance(data, dict):
        if data.get("id") is not None:
            return data.get("id")
        nested = data.get("diagnos_data")
        if isinstance(nested, dict):
            return nested.get("id")
    if isinstance(data, list) and data and isinstance(data[0], dict):
        return data[0].get("id")
    return response_json.get("id")


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
                    "title": "Test diagnos",
                    "status": "ACTIVE",
                }
            }
        with allure.step("Создание диагноза"):
            response = self.diagnoses.post_diagnos(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response

    def update_diagnos(self, diagnos_id=None, json_data=None):
        if diagnos_id is None:
            with allure.step("Подготовка: создание диагноза для update"):
                response_create = self.create_diagnos()
                diagnos_id = _get_id_from_response(response_create)
            assert diagnos_id is not None, (
                f"Не удалось извлечь id из ответа создания: {getattr(response_create, 'response_json', None)}"
            )
        if json_data is None:
            json_data = {
                "diagnos_data": {
                    "title": "Update diagnos",
                    "status": "ACTIVE",
                }
            }
        with allure.step("Обновление диагноза"):
            response = self.diagnoses.patch_diagnos(diagnos_id, json_data)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def delete_diagnos(self, diagnos_id=None):
        if diagnos_id is None:
            with allure.step("Подготовка: создание диагноза для delete"):
                response_create = self.create_diagnos()
                diagnos_id = _get_id_from_response(response_create)
            assert diagnos_id is not None, (
                f"Не удалось извлечь id из ответа создания: {getattr(response_create, 'response_json', None)}"
            )
        with allure.step("Удаление диагноза"):
            response = self.diagnoses.delete_diagnos(diagnos_id)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response
