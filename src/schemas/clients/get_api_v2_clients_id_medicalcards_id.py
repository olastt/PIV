from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdMedicalcardsIdResponseDoctorData(StrictResponseModel):
    doctor_id: Any
    doctor_nickname: Any
    first_name: Any
    last_name: Any
    middle_name: Any

class GetApiV2ClientsIdMedicalcardsIdResponsePetData(StrictResponseModel):
    pet_id: Any
    alias: Any
    birthday: Any
    sex: Any
    note: Any
    pet_type: Any
    breed: Any

class GetApiV2ClientsIdMedicalcardsIdResponseClientData(StrictResponseModel):
    client_id: Any
    first_name: Any
    last_name: Any
    middle_name: Any
    phone: Any

class GetApiV2ClientsIdMedicalcardsIdResponseAdmissionData(StrictResponseModel):
    id: Any
    admission_date: Any
    description: Any
    client_id: Any
    patient_id: Any
    user_id: Any
    type_id: Any
    admission_length: Any
    status: Any
    clinic_id: Any
    direct_direction: Any
    creator_id: Any
    create_date: Any
    escorter_id: Any
    reception_write_channel: Any
    is_auto_create: Any
    invoices_sum: Any
    confirmation: Any
    wait_time: Any
    icon_reception_write_channel: Any

class GetApiV2ClientsIdMedicalcardsIdResponse(StrictResponseModel):
    medical_card_id: Any
    date: Any
    doctor_nickname: Any
    first_name: Any
    last_name: Any
    middle_name: Any
    medical_card_status: Any
    healing_process: Any
    recomendation: Any
    weight: Any
    temperature: Any
    meet_result_id: Any
    admission_type: Any
    meet_result_title: Any
    admission_type_title: Any
    doctor_data: GetApiV2ClientsIdMedicalcardsIdResponseDoctorData
    pet_data: GetApiV2ClientsIdMedicalcardsIdResponsePetData
    client_data: GetApiV2ClientsIdMedicalcardsIdResponseClientData
    admission_data: GetApiV2ClientsIdMedicalcardsIdResponseAdmissionData
    diagnos_data: list[Any]
    basis_for_admission: Any
    admission_id: Any
    styles_content: Any
    styles_content_images: Any
    editable: Any

