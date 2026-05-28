from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PatchApiV2HospitalIdResponseDataHospitalDataPetData(StrictResponseModel):
    id: Any
    owner_id: Any
    type_id: Any
    alias: Any
    sex: Any
    date_register: Any
    birthday: Optional[Any] = None
    note: Any
    breed_id: Optional[Any] = None
    old_id: Optional[Any] = None
    color_id: Optional[Any] = None
    deathnote: Optional[Any] = None
    deathdate: Optional[Any] = None
    chip_number: Any
    lab_number: Any
    status: Any
    picture: Optional[Any] = None
    weight: Any
    edit_date: Any

class PatchApiV2HospitalIdResponseDataHospitalDataDoctorData(StrictResponseModel):
    id: Any
    last_name: Any
    first_name: Any
    middle_name: Any
    login: Any
    passwd: Any
    position_id: Any
    email: Any
    phone: Any
    cell_phone: Any
    address: Any
    role_id: Any
    is_active: Any
    calc_percents: Any
    nickname: Any
    last_change_pwd_date: Any
    is_limited: Any
    sip_number: Any
    user_inn: Any

class PatchApiV2HospitalIdResponseDataHospitalData(StrictResponseModel):
    id: Any
    client_id: Any
    pet_id: Any
    user_id: Any
    invoice_id: Any
    start_date: Any
    end_date: Any
    place: Any
    description: Any
    hospital_block_id: Any
    clinic_id: Any
    admission_id: Any
    status: Any
    pet_data: PatchApiV2HospitalIdResponseDataHospitalDataPetData
    doctor_data: PatchApiV2HospitalIdResponseDataHospitalDataDoctorData

class PatchApiV2HospitalIdResponseData(StrictResponseModel):
    hospital_data: PatchApiV2HospitalIdResponseDataHospitalData

class PatchApiV2HospitalIdResponse(StrictResponseModel):
    message: Any
    data: PatchApiV2HospitalIdResponseData

