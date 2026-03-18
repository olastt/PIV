import allure
import pytest
from Library.MakeyIS import Test


def _get_id_from_response(response):
    """Извлекает id из ответа API (data.id, data.diagnos_data.id, data[0].id или id в корне)."""
    if not response or not getattr(response, "response_json", None):
        return None
    j = response.response_json
    data = j.get("data")
    if isinstance(data, dict):
        # data.id или вложенный data.diagnos_data.id (ответ создания диагноза)
        out = data.get("id")
        if out is not None:
            return out
        inner = data.get("diagnos_data") or data.get("call_data")
        if isinstance(inner, dict):
            return inner.get("id")
    if isinstance(data, list) and data:
        return data[0].get("id") if isinstance(data[0], dict) else None
    return j.get("id")


class TestDiagnosesPositive:

    @pytest.mark.positive
    @allure.epic('Диагнозы')
    @allure.feature('GET /api/v2/diagnoses')
    @allure.title('Получение списка всех диагнозов')
    @Test(run_test=True, group_name="Диагнозы", log=True)
    def test_get_diagnoses(self, diagnoses_start):
        diagnoses_start.get_diagnoses()

    @pytest.mark.positive
    @allure.epic('Диагнозы')
    @allure.feature('GET /api/v2/diagnoses/{diagnos_id}')
    @allure.title('Получение данных по диагнозу')
    @Test(run_test=True, group_name="Диагнозы", log=True)
    def test_get_diagnos_by_id(self, diagnoses_start):
        diagnoses_start.get_diagnos_by_id(diagnos_id=1)

    @pytest.mark.positive
    @allure.epic('Диагнозы')
    @allure.feature('POST /api/v2/diagnoses -> PATCH -> DELETE')
    @allure.title('Цепочка: создание диагноза -> обновление -> удаление (по id из ответа)')
    def test_diagnos_create_update_delete_flow(self, diagnoses_start):
        response_create = diagnoses_start.create_diagnos()
        diagnos_id = _get_id_from_response(response_create)
        assert diagnos_id is not None, (
            f"Не удалось извлечь id из ответа создания: {getattr(response_create, 'response_json', None)}"
        )
        diagnoses_start.update_diagnos(diagnos_id=diagnos_id)
        diagnoses_start.delete_diagnos(diagnos_id=diagnos_id)
