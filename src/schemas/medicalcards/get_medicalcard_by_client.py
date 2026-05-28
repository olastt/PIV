from typing import Any

from pydantic import StrictBool, StrictInt, StrictStr

from src.schemas.medicalcards.common import (
    AdmissionData,
    ClientData,
    DoctorData,
    PetData,
    StrictResponseModel,
)


class MedicalcardDetailResponse(StrictResponseModel):
    medical_card_id: StrictInt
    date: StrictStr
    doctor_nickname: StrictStr
    first_name: StrictStr
    last_name: StrictStr
    middle_name: StrictStr
    medical_card_status: StrictStr
    healing_process: StrictStr
    recomendation: StrictStr
    weight: StrictInt
    temperature: StrictInt
    meet_result_id: StrictInt
    admission_type: StrictInt
    meet_result_title: StrictStr
    admission_type_title: StrictStr
    doctor_data: DoctorData
    pet_data: PetData
    client_data: ClientData
    admission_data: AdmissionData
    diagnos_data: list[Any]
    basis_for_admission: StrictStr
    admission_id: StrictInt
    styles_content: StrictStr
    styles_content_images: StrictStr
    editable: StrictBool
