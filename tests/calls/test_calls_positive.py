import allure
import pytest
from Library.MakeyIS import Test


# def _get_id_from_response(response):
#     """Извлекает id из ответа API (data.id, data.call_data.id, data[0].id или id в корне)."""
#     if not response or not getattr(response, "response_json", None):
#         return None
#     j = response.response_json
#     data = j.get("data")
#     if isinstance(data, dict):
#         out = data.get("id")
#         if out is not None:
#             return out
#         inner = data.get("call_data") or data.get("diagnos_data")
#         if isinstance(inner, dict):
#             return inner.get("id")
#     if isinstance(data, list) and data:
#         return data[0].get("id") if isinstance(data[0], dict) else None
#     return j.get("id")


# def _get_call_id_from_list_response(response):
#     """Извлекает id прозвона из ответа GET списка (первый элемент или с макс. id)."""
#     if not response or not getattr(response, "response_json", None):
#         return None
#     j = response.response_json
#     # Ответ может быть списком на верхнем уровне или {"data": [...]}
#     if isinstance(j, list) and j:
#         data = j
#     elif isinstance(j, dict):
#         data = j.get("data")
#     else:
#         return None
#     if isinstance(data, list) and data:
#         first = data[0] if isinstance(data[0], dict) else None
#         if first and "id" in first:
#             return first.get("id")
#         ids = [x.get("id") for x in data if isinstance(x, dict) and x.get("id") is not None]
#         return max(ids) if ids else None
#     return None


class TestCallsPositive:
    @pytest.mark.positive
    @allure.epic('Звонки')
    @allure.feature('GET /api/v2/users/{user_id}/calls')
    @allure.title('Получение прозвонов, которые должен совершить пользователь')
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_get_user_calls(self, calls_start):
        calls_start.get_user_calls()

    @pytest.mark.positive
    @allure.epic('Звонки')
    @allure.feature('GET /api/v2/calls/search')
    @allure.title('Поиск выполненных звонков')
    @Test(run_test=True, group_name="Звонки", log=True)
    def test_get_calls_search(self, calls_start):
        calls_start.get_calls_search()

    # @pytest.mark.positive
    # @allure.epic('Звонки')
    # @allure.feature('POST /api/v2/users/{user_id}/calls -> PATCH')
    # @allure.title('Цепочка: создание прозвона -> обновление (по call_id из ответа)')
    # def test_call_create_and_update_flow(self, calls_start):
    #     response_create = calls_start.create_user_call()
    #     call_id = _get_id_from_response(response_create)
    #     if call_id is None:
    #         # API прозвонов не возвращает id в ответе создания — берём из списка после создания
    #         response_list = calls_start.get_user_calls()
    #         call_id = _get_call_id_from_list_response(response_list)
    #     assert call_id is not None, (
    #         f"Не удалось получить call_id: ни из ответа создания {getattr(response_create, 'response_json', None)}, "
    #         "ни из списка прозвонов"
    #     )
    #     calls_start.update_user_call(call_id=call_id)

    @pytest.mark.positive
    @allure.epic('Звонки')
    @allure.feature('GET /api/v2/users/{user_id}/calls/{call_id}')
    @allure.title('Получение прозвона по ID')
    def test_get_user_call_by_id(self, calls_start):
        calls_start.get_user_call_by_id()
