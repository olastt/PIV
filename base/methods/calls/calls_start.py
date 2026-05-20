import time

import allure
from base.methods.calls.calls_methods import CallsMethods


def _call_id_from_response(response):
    """Извлекает call_id из ответа POST create (корень, data, call_data)."""
    if not response or not getattr(response, "response_json", None):
        return None
    body = response.response_json
    if not isinstance(body, dict):
        return None

    for key in ("call_id", "id"):
        val = body.get(key)
        if val is not None:
            return int(val)

    data = body.get("data")
    if isinstance(data, dict):
        for key in ("call_id", "id"):
            val = data.get(key)
            if val is not None:
                return int(val)
        call_data = data.get("call_data")
        if isinstance(call_data, dict):
            for key in ("call_id", "id"):
                val = call_data.get(key)
                if val is not None:
                    return int(val)
    return None


def _call_items_from_list_response(response):
    if not response or not getattr(response, "response_json", None):
        return []
    body = response.response_json
    if isinstance(body, list):
        return [x for x in body if isinstance(x, dict)]
    if not isinstance(body, dict):
        return []
    data = body.get("data")
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    if isinstance(data, dict):
        for key in ("items", "calls", "results"):
            nested = data.get(key)
            if isinstance(nested, list):
                return [x for x in nested if isinstance(x, dict)]
    return []


def _item_note(item):
    if item.get("note") is not None:
        return item.get("note")
    call_data = item.get("call_data")
    if isinstance(call_data, dict) and call_data.get("note") is not None:
        return call_data.get("note")
    return None


def _item_call_id(item):
    for key in ("call_id", "id"):
        if item.get(key) is not None:
            return int(item[key])
    call_data = item.get("call_data")
    if isinstance(call_data, dict):
        for key in ("call_id", "id"):
            if call_data.get(key) is not None:
                return int(call_data[key])
    return None


def _call_id_from_list_response(response, note=None):
    """Извлекает call_id из GET списка (по note или максимальный id)."""
    items = _call_items_from_list_response(response)
    if not items:
        return None

    if note is not None:
        for item in items:
            if _item_note(item) == note:
                call_id = _item_call_id(item)
                if call_id is not None:
                    return call_id

    ids = [_item_call_id(item) for item in items]
    ids = [x for x in ids if x is not None]
    return max(ids) if ids else None


def resolve_call_id_after_create(calls_start, user_id, create_response, note):
    """call_id из тела POST или из списка прозвонов после создания."""
    call_id = _call_id_from_response(create_response)
    if call_id is not None:
        return call_id

    for attempt in range(5):
        list_response = calls_start.get_user_calls(
            user_id=user_id,
            filter_status="save",
            page_number=1,
            page_size=50,
        )
        call_id = _call_id_from_list_response(list_response, note=note)
        if call_id is not None:
            return call_id
        if attempt < 4:
            time.sleep(0.5)

    search_response = calls_start.get_calls_search(
        user_id=user_id,
        status="save",
        page_number=1,
        page_size=50,
    )
    return _call_id_from_list_response(search_response, note=note)


class CallsStart:
    """Стартовые сценарии для Calls."""

    def __init__(self):
        self.calls = CallsMethods()
        self.update_call_user_id = None
        self.update_call_id = None

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

    def create_user_call(self, user_id=1, json_data=None):
        if json_data is None:
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

    def update_user_call(self, user_id=None, call_id=None, json_data=None):
        if user_id is None:
            user_id = self.update_call_user_id if self.update_call_user_id is not None else 1
        if call_id is None:
            call_id = self.update_call_id
        assert call_id is not None, (
            "call_id не задан: подключите фикстуру call_for_update"
        )
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
