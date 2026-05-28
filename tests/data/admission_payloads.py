import os
from datetime import datetime, timedelta


CREATE_ADMISSION_START_HOUR = 8
CREATE_ADMISSION_END_HOUR = 22
CREATE_ADMISSION_STEP_MINUTES = 15
CREATE_ADMISSION_SLOTS_PER_DAY = (
    (CREATE_ADMISSION_END_HOUR - CREATE_ADMISSION_START_HOUR) * 60
) // CREATE_ADMISSION_STEP_MINUTES


def _first_available_admission_slot() -> datetime:
    now = datetime.now()
    day_start = now.replace(
        hour=CREATE_ADMISSION_START_HOUR,
        minute=0,
        second=0,
        microsecond=0,
    )
    day_end = now.replace(
        hour=CREATE_ADMISSION_END_HOUR,
        minute=0,
        second=0,
        microsecond=0,
    )

    if now < day_start:
        return day_start

    if now >= day_end:
        return day_start + timedelta(days=1)

    minutes_from_start = int((now - day_start).total_seconds() // 60)
    next_slot_number = (minutes_from_start // CREATE_ADMISSION_STEP_MINUTES) + 1
    return day_start + timedelta(minutes=next_slot_number * CREATE_ADMISSION_STEP_MINUTES)


def default_create_admission_payload(slot: int) -> dict:
    day_offset, slot_in_day = divmod(slot, CREATE_ADMISSION_SLOTS_PER_DAY)
    base_slot = _first_available_admission_slot()
    admission_date = (
        base_slot + timedelta(days=day_offset, minutes=CREATE_ADMISSION_STEP_MINUTES * slot_in_day)
    ).strftime("%Y-%m-%d %H:%M:%S")
    return {
        "admission_data": {
            "admission_type_id": int(os.getenv("ADMISSION_TYPE_ID", "4")),
            "admission_date": admission_date,
            "user_id": int(os.getenv("ADMISSION_DOCTOR_ID", "1")),
            "clinic_id": int(os.getenv("CLINIC_ID", "1")),
            "client_id": int(os.getenv("ADMISSION_CLIENT_ID", "193")),
            "pet_id": int(os.getenv("ADMISSION_PET_ID", "100")),
            "status": os.getenv("ADMISSION_STATUS", "save"),
            "description": "test admission",
            "admission_length": "00:15:00",
        }
    }
