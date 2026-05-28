from typing import Any

from pydantic import StrictBool, StrictInt, StrictStr

from src.schemas.medicalcards.common import ClientData, DoctorData, PetData, StrictResponseModel


class MedicalcardListItem(StrictResponseModel):
    medical_card_id: StrictInt
    date: StrictStr
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
    diagnos_data: list[Any]
    editable: StrictBool


GetMedicalcardsByClientResponse = list[MedicalcardListItem]
