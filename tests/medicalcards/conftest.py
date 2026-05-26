import os

import pytest

from base.methods.medicalcards.medicalcards_start import build_default_post_medicalcard_vaccination_json


@pytest.fixture
def patch_medicalcard_vaccination_json_data():
    medicalcard_id = int(os.getenv("MEDICALCARD_ID", "1"))
    return {
        "vaccination_data": {
            "medcard_id": medicalcard_id,
            "pet_id": int(os.getenv("PET_ID", "1")),
            "clinic_id": int(os.getenv("CLINIC_ID", "1")),
            "doctor_id": int(os.getenv("DOCTOR_ID", "1")),
            "vaccine_id": os.getenv("VACCINE_ID_STRING", "1_1"),
            "vaccine_type": int(os.getenv("VACCINE_TYPE", "1")),
            "doza_value": int(os.getenv("VACCINE_DOZA_VALUE", "1")),
            "vaccine_date": os.getenv("VACCINE_DATE", "2026-02-12 15:30"),
            "delete_vaccine_nextdates": False,
            "plane_next_visit_by_repead_vaccine_date": True,
            "vaccine_description": os.getenv("VACCINE_DESCRIPTION", "test postman"),
            "next_date": os.getenv("VACCINE_NEXT_DATE", "2026-11-12"),
            "next_visit_time": os.getenv("VACCINE_NEXT_VISIT_TIME", "15:50:00"),
            "pet_weight": int(os.getenv("PET_WEIGHT", "5")),
            "pet_temperature": int(os.getenv("PET_TEMPERATURE", "36")),
        }
    }


@pytest.fixture
def post_medicalcard_vaccination_json_data():
    return build_default_post_medicalcard_vaccination_json()
