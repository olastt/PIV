import itertools
import os

import allure
from base.methods.admission.admission_methods import AdmissionMethods
from tests.data.admission_payloads import CREATE_ADMISSION_SLOTS_PER_DAY, default_create_admission_payload

# Сдвиг даты на 15 минут на каждый дефолтный create, чтобы не пытаться повторно занять тот же слот.
_create_admission_slot = itertools.count()


def _admission_id_from_response_body(body: dict) -> int:
    """Извлекает id приёма из тела ответа POST create с учётом разных форматов API."""
    if not isinstance(body, dict):
        raise AssertionError(f"Ожидался dict в response_json, получено: {type(body)!r}")

    for key in ("admission_id", "id"):
        val = body.get(key)
        if val is not None:
            return int(val)

    data = body.get("data")
    if isinstance(data, dict):
        for key in ("id", "admission_id"):
            val = data.get(key)
            if val is not None:
                return int(val)
        for nested_key in ("admission", "admission_data"):
            nested = data.get(nested_key)
            if isinstance(nested, dict):
                for key in ("id", "admission_id"):
                    val = nested.get(key)
                    if val is not None:
                        return int(val)

    raise AssertionError(f"В ответе не найден id приёма: {body}")


def _is_retryable_create_error(exc: Exception) -> bool:
    text = str(exc)
    retryable_markers = (
        "UNEXPECTED_EOF_WHILE_READING",
        "Request error during POST",
        "ConnectError",
        "connection reset",
        "Connection aborted",
        "Temporary failure",
    )
    return any(marker in text for marker in retryable_markers)


def _response_text(response) -> str:
    response_json = getattr(response, "response_json", None)
    if response_json is not None:
        return str(response_json).lower()
    response_text = getattr(response, "response_text", None)
    if response_text:
        return str(response_text).lower()
    raw_response = getattr(response, "response", None)
    return str(getattr(raw_response, "text", "")).lower()


def _is_busy_admission_slot(response) -> bool:
    if getattr(response, "response_status", None) not in (400, 409, 422, 500, 520):
        return False

    if getattr(response, "response_status", None) == 520:
        return True

    text = _response_text(response)
    busy_markers = (
        "занят",
        "занято",
        "занята",
        "место",
        "слот",
        "time is busy",
        "already booked",
        "already exists",
        "busy",
    )
    return any(marker in text for marker in busy_markers)


def _admission_id_from_create_response(response) -> int:
    if response.response_json is None:
        raise AssertionError("В ответе нет JSON (response_json is None)")
    return _admission_id_from_response_body(response.response_json)


class AdmissionStart:

    def __init__(self):
        self.admission = AdmissionMethods()

    def get_admission_by_id(
        self,
        admission_id=1,
        clinic_id=1,
        page_number=1,
        page_size=20,
        filter_status="save",
        params=None,
    ):
        if params is None:
            params = {
                "clinic_id": clinic_id,
                "page[number]": page_number,
                "page[size]": page_size,
                "filter[status]": filter_status,
            }
        with allure.step("Запрос приёма по ID"):
            response = self.admission.get_admission_by_id(admission_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_admissions_by_user(self, user_id=1, clinic_id=1, page_number=1, page_size=20, filter_status="save"):
        params = {
            "clinic_id": clinic_id,
            "page[number]": page_number,
            "page[size]": page_size,
            "filter[status]": filter_status,
        }
        with allure.step("Запрос приёмов пользователя"):
            response = self.admission.get_admissions_by_user(user_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def create_admission(self, user_id=None, json_data=None):
        user_id = user_id or int(os.getenv("ADMISSION_PATH_USER_ID", "16"))
        use_default_payload = json_data is None
        max_attempts = CREATE_ADMISSION_SLOTS_PER_DAY if use_default_payload else 1
        response = None
        last_exc = None

        for attempt in range(max_attempts):
            current_json = json_data
            if use_default_payload:
                slot = next(_create_admission_slot)
                current_json = default_create_admission_payload(slot)

            try:
                with allure.step("POST /api/v2/users/{user_id}/admission"):
                    response = self.admission.create_admission(user_id, json_data=current_json)
            except Exception as exc:
                last_exc = exc
                if attempt == max_attempts - 1 or not _is_retryable_create_error(exc):
                    raise
                with allure.step(f"Повтор create_admission после transport error, попытка {attempt + 2}"):
                    pass
                continue

            if response.response_status == 200:
                break

            if not use_default_payload or not _is_busy_admission_slot(response):
                break

            with allure.step(f"Повтор create_admission после {response.response_status}, попытка {attempt + 2}"):
                pass

        if response is None and last_exc is not None:
            raise last_exc

        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response

    def patch_admission(self, user_id=1, admission_id=None, json_data=None):
        if admission_id is None:
            with allure.step("Подготовка: создание приёма для PATCH"):
                create_resp = self.create_admission(user_id=user_id)
                admission_id = _admission_id_from_create_response(create_resp)
        if json_data is None:
            json_data = {
                "admission_data": {
                    "admission_type_id": 4,
                    "admission_date": "2026-05-02 09:00:00",
                    "user_id": 1,
                    "clinic_id": 1,
                    "client_id": 193,
                    "pet_id": 100,
                    "status": "accepted",
                    "description": "тест удаление",
                    "admission_length": "00:15:00",
                }
            }
        with allure.step("PATCH /api/v2/users/{user_id}/admission/{admission_id}"):
            response = self.admission.patch_admission(user_id, admission_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code(200)
        return response

    def confirm_admission(self, user_id=None, admission_id=None, json_data=None):
        user_id = user_id or int(os.getenv("ADMISSION_PATH_USER_ID", "16"))
        if admission_id is None:
            with allure.step("Create admission for confirm"):
                create_resp = self.create_admission(user_id=user_id)
                admission_id = _admission_id_from_create_response(create_resp)
        if json_data is None:
            payload = default_create_admission_payload(next(_create_admission_slot))
            admission_data = payload["admission_data"]
            json_data = {
                "admission_data": {
                    "type_id": admission_data["admission_type_id"],
                    "admission_date": admission_data["admission_date"],
                    "user_id": admission_data["user_id"],
                    "clinic_id": admission_data["clinic_id"],
                    "client_id": admission_data["client_id"],
                    "patient_id": admission_data["pet_id"],
                    "description": "pytest confirm admission",
                }
            }
        with allure.step("POST /api/v2/users/admission/{admission_id}/confirm"):
            response = self.admission.post_admission_confirm(admission_id, json_data=json_data)
        with allure.step("Check status code"):
            response.assert_status_code(200)
        return response
    #
