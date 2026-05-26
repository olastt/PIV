import os

import allure
from base.methods.medicalcards.medicalcards_methods import MedicalcardsMethods


def _extract_vaccination_id_from_response(response):
    if not response or not getattr(response, "response_json", None):
        return None

    response_json = response.response_json
    data = response_json.get("data")
    if isinstance(data, dict):
        for key in ("id", "vaccination_id"):
            if data.get(key) is not None:
                return data.get(key)
        nested = data.get("vaccination_data")
        if isinstance(nested, dict):
            for key in ("id", "vaccination_id"):
                if nested.get(key) is not None:
                    return nested.get(key)
    if isinstance(data, list) and data and isinstance(data[0], dict):
        return data[0].get("id") or data[0].get("vaccination_id")
    return response_json.get("id") or response_json.get("vaccination_id")


def build_default_post_medicalcard_vaccination_json(
    medicalcard_id: int = None,
    pet_id: int = None,
) -> dict:
    """Тело POST вакцинации (как в tests/medicalcards/conftest.py)."""
    medicalcard_id = medicalcard_id or int(os.getenv("MEDICALCARD_ID", "1"))
    pet_id = pet_id or int(os.getenv("PET_ID", "1"))
    return {
        "vaccination_data": {
            "medcard_id": medicalcard_id,
            "pet_id": pet_id,
            "clinic_id": int(os.getenv("CLINIC_ID", "1")),
            "doctor_id": int(os.getenv("DOCTOR_ID", "1")),
            "vaccine_id": int(os.getenv("VACCINE_ID", "1")),
            "vaccine_type": int(os.getenv("VACCINE_TYPE", "1")),
            "doza_value": int(os.getenv("VACCINE_DOZA_VALUE", "1")),
            "vaccine_date": os.getenv("VACCINE_DATE", "2025-11-12 15:57"),
            "delete_vaccine_nextdates": False,
            "plane_next_visit_by_repead_vaccine_date": True,
            "vaccine_description": os.getenv("VACCINE_DESCRIPTION", "test postman"),
            "next_date": os.getenv("VACCINE_NEXT_DATE", "2026-11-12"),
            "next_visit_time": os.getenv("VACCINE_NEXT_VISIT_TIME", "15:50:00"),
            "pet_weight": int(os.getenv("PET_WEIGHT", "0")),
            "pet_temperature": int(os.getenv("PET_TEMPERATURE", "0")),
        }
    }


class MedicalcardsStart:
    """Стартовые сценарии для Medicalcards (коллекция Postman: Medicalcards, Vaccinations)."""

    # id последней успешно созданной вакцинации (между test_post_* и test_patch_* в одном прогоне)
    _last_vaccination_id = None

    def __init__(self):
        self.medicalcards = MedicalcardsMethods()

    def get_medicalcards_diagnoses(self, params=None):
        with allure.step("Запрос диагнозов для медкарт"):
            response = self.medicalcards.get_medicalcards_diagnoses()
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_vaccinations_by_pet(self, pet_id: int = None):
        pet_id = pet_id or int(os.getenv("PET_ID", "1"))
        with allure.step("GET /api/v2/medicalcards/vaccinations/{pet_id}"):
            response = self.medicalcards.get_vaccinations_by_pet(pet_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_medicalcards_by_client(self, client_id: int = None, page_number=1, page_size=10):
        client_id = client_id or int(os.getenv("CLIENT_ID", "1"))
        params = {"page[number]": page_number, "page[size]": page_size}
        with allure.step("GET /api/v2/clients/{client_id}/medicalcards"):
            response = self.medicalcards.get_medicalcards_by_client(client_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_medicalcard_by_client(self, client_id: int = None, medicalcard_id: int = None):
        client_id = client_id or int(os.getenv("CLIENT_ID", "1"))
        medicalcard_id = medicalcard_id or int(os.getenv("MEDICALCARD_ID", "1"))
        with allure.step("GET /api/v2/clients/{client_id}/medicalcards/{medicalcard_id}"):
            response = self.medicalcards.get_medicalcard_by_client(client_id, medicalcard_id)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_medicalcard_text_templates(self, params=None):
        with allure.step("GET /api/v2/medicalcards/texttemplates"):
            response = self.medicalcards.get_medicalcard_text_templates(params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def get_medicalcards_history(self, client_id: int = None, params=None):
        client_id = client_id or int(os.getenv("CLIENT_ID", "1"))
        with allure.step("GET /api/v2/clients/{client_id}/medicalcards/history"):
            response = self.medicalcards.get_medicalcards_history(client_id, params=params)
        with allure.step("Проверка статус кода 200"):
            response.assert_status_code(200)
        return response

    def post_medicalcards_uploadfiles(self, json_data: dict = None):
        with allure.step("POST /api/v2/medicalcards/uploadfiles"):
            response = self.medicalcards.post_medicalcards_uploadfiles(json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        return response

    # def post_medicalcards_generate_llm(self, json_data: dict = None):
    #     if json_data is None:
    #         json_data = {"prompt": "test", "clinic_id": int(os.getenv("CLINIC_ID", "1"))}
    #     with allure.step("POST /api/v2/medicalcards/generate-llm"):
    #         response = self.medicalcards.post_medicalcards_generate_llm(json_data)
    #     with allure.step("Проверка статус кода"):
    #         response.assert_status_code([200, 201, 422, 503])
    #     return response

    def post_medicalcards_generate_llm(self, json_data: dict = None):
        if json_data is None:
            json_data = {"transcription": "Мой кот Борис плохо ест"}
        with allure.step("POST /api/v2/medicalcards/generate-llm"):
            response = self.medicalcards.post_medicalcards_generate_llm(json_data)
        with allure.step("Check status code"):
            response.assert_status_code([200, 201, 422, 503])
        return response

    def post_create_medicalcard(self, client_id: int = None, json_data: dict = None):
        client_id = client_id or int(os.getenv("CLIENT_ID", "1"))
        pet_id = int(os.getenv("PET_ID", "1"))
        if json_data is None:
            json_data = {
                "medicalcard_data": {
                    "pet_id": pet_id,
                    "doctor_id": int(os.getenv("DOCTOR_ID", "1")),
                    "clinic_id": int(os.getenv("CLINIC_ID", "1")),
                    "healing_overview": "pytest medicalcard",
                    "recomendation": "рекомендация",
                    "date_create": "2026-01-15 12:00:00",
                    "reason_visit_id": int(os.getenv("REASON_VISIT_ID", "4")),
                    "meet_result_id": int(os.getenv("MEET_RESULT_ID", "3")),
                    "weight": 5,
                    "temperature": 36,
                    "diagnos": [{"id": int(os.getenv("DIAGNOS_ID_FOR_MC", "1"))}],
                }
            }
        with allure.step("POST /api/v2/clients/{client_id}/medicalcards"):
            response = self.medicalcards.post_create_medicalcard(client_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        return response

    def patch_medicalcard(self, client_id: int = None, medicalcard_id: int = None, json_data: dict = None):
        client_id = client_id or int(os.getenv("CLIENT_ID", "1"))
        medicalcard_id = medicalcard_id or int(os.getenv("MEDICALCARD_ID", "1"))
        if json_data is None:
            json_data = {"medicalcard_data": {"healing_overview": "pytest patch overview"}}
        with allure.step("PATCH медкарты"):
            response = self.medicalcards.patch_medicalcard(client_id, medicalcard_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        return response

    def post_medicalcard_vaccination(self, medicalcard_id: int = None, pet_id: int = None, json_data: dict = None):
        medicalcard_id = medicalcard_id or int(os.getenv("MEDICALCARD_ID", "1"))
        pet_id = pet_id or int(os.getenv("PET_ID", "1"))
        if json_data is None:
            raise AssertionError(
                "Для POST вакцинации передайте json_data "
                "(используйте фикстуру post_medicalcard_vaccination_json_data из tests/medicalcards/conftest.py)"
            )
        with allure.step("POST вакцинации к медкарте"):
            response = self.medicalcards.post_medicalcard_vaccination(medicalcard_id, pet_id, json_data)
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        if response.response_status in (200, 201):
            vid = _extract_vaccination_id_from_response(response)
            if vid is not None:
                MedicalcardsStart._last_vaccination_id = vid
        return response

    def patch_medicalcard_vaccination(
        self,
        medicalcard_id: int = None,
        vaccination_id: int = None,
        *,
        pet_id: int = None,
        create_json_data: dict = None,
        json_data: dict = None,
    ):
        medicalcard_id = medicalcard_id or int(os.getenv("MEDICALCARD_ID", "1"))
        pet_id = pet_id or int(os.getenv("PET_ID", "1"))

        if vaccination_id is None:
            if MedicalcardsStart._last_vaccination_id is not None:
                vaccination_id = MedicalcardsStart._last_vaccination_id
                with allure.step("Использование vaccination_id из последнего POST вакцинации"):
                    pass
            else:
                payload = create_json_data or build_default_post_medicalcard_vaccination_json(
                    medicalcard_id, pet_id
                )
                with allure.step(
                    "Подготовка: POST вакцинации для PATCH "
                    "(нет сохранённого id — одиночный запуск или POST не вернул id)"
                ):
                    response_create = self.post_medicalcard_vaccination(
                        medicalcard_id=medicalcard_id,
                        pet_id=pet_id,
                        json_data=payload,
                    )
                    vaccination_id = _extract_vaccination_id_from_response(response_create)
                assert vaccination_id is not None, (
                    f"Не удалось извлечь vaccination_id из ответа создания: "
                    f"{getattr(response_create, 'response_json', None)}"
                )

        if json_data is None:
            json_data = {
                "vaccination_data": {
                    "medcard_id": medicalcard_id,
                    "pet_id": pet_id,
                    "clinic_id": int(os.getenv("CLINIC_ID", "1")),
                    "doctor_id": int(os.getenv("DOCTOR_ID", "1")),
                    "vaccine_id": os.getenv("VACCINE_ID_STRING", "1_1"),
                    "vaccine_type": int(os.getenv("VACCINE_TYPE", "1")),
                    "doza_value": int(os.getenv("VACCINE_DOZA_VALUE", "1")),
                    "vaccine_date": os.getenv("VACCINE_DATE", "2025-11-12 15:57"),
                    "delete_vaccine_nextdates": False,
                    "plane_next_visit_by_repead_vaccine_date": True,
                    "vaccine_description": os.getenv("VACCINE_DESCRIPTION", "test postman"),
                    "next_date": os.getenv("VACCINE_NEXT_DATE", "2026-11-12"),
                    "next_visit_time": os.getenv("VACCINE_NEXT_VISIT_TIME", "15:50:00"),
                    "pet_weight": int(os.getenv("PET_WEIGHT", "0")),
                    "pet_temperature": int(os.getenv("PET_TEMPERATURE", "0")),
                }
            }

        with allure.step("PATCH вакцинации (полный путь V2)"):
            response = self.medicalcards.patch_medicalcard_vaccination(
                medicalcard_id, vaccination_id, json_data
            )
        with allure.step("Проверка статус кода"):
            response.assert_status_code([200, 201, 422])
        return response
