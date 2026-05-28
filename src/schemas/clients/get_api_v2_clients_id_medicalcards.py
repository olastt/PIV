from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdMedicalcardsItemDoctorData(StrictResponseModel):
    doctor_id: Any
    doctor_nickname: Any
    first_name: Any
    last_name: Any
    middle_name: Any

class GetApiV2ClientsIdMedicalcardsItemPetData(StrictResponseModel):
    pet_id: Any
    alias: Any
    birthday: Any
    sex: Any
    note: Any
    pet_type: Any
    breed: Any

class GetApiV2ClientsIdMedicalcardsItemClientData(StrictResponseModel):
    client_id: Any
    first_name: Any
    last_name: Any
    middle_name: Any
    phone: Any

class GetApiV2ClientsIdMedicalcardsItem(StrictResponseModel):
    medical_card_id: Any
    date: Any
    medical_card_status: Any
    healing_process: Any
    recomendation: Any
    weight: Any
    temperature: Any
    meet_result_id: Any
    admission_type: Any
    meet_result_title: Any
    admission_type_title: Any
    doctor_data: GetApiV2ClientsIdMedicalcardsItemDoctorData
    pet_data: GetApiV2ClientsIdMedicalcardsItemPetData
    client_data: GetApiV2ClientsIdMedicalcardsItemClientData
    diagnos_data: list[Any]
    editable: Any


class GetApiV2ClientsIdMedicalcardsResponse(RootModel[list[GetApiV2ClientsIdMedicalcardsItem]]):
    pass

