from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2HospitalIdResponseDataPetData(StrictResponseModel):
    pet_id: Any
    sex: Any
    alias: Any
    pet_type: Any
    birthday: Any
    pet_type_id: Any
    pet_breed: Any
    weight: Any
    url: Any

class GetApiV2HospitalIdResponseDataClientData(StrictResponseModel):
    client_id: Any
    first_name: Any
    middle_name: Any
    last_name: Any
    email: Any
    cell_phone: Any
    address: Any
    in_blacklist: Any

class GetApiV2HospitalIdResponseDataDoctorData(StrictResponseModel):
    doctor_id: Any
    last_name: Any
    first_name: Any
    middle_name: Any
    nickname: Any

class GetApiV2HospitalIdResponseData(StrictResponseModel):
    id: Any
    client_id: Any
    pet_id: Any
    user_id: Any
    invoice_id: Any
    start_date: Any
    end_date: Optional[Any] = None
    place: Any
    description: Any
    hospital_block_id: Any
    clinic_id: Any
    admission_id: Any
    status: Any
    in_hospital_time: Any
    pet_data: GetApiV2HospitalIdResponseDataPetData
    client_data: GetApiV2HospitalIdResponseDataClientData
    doctor_data: GetApiV2HospitalIdResponseDataDoctorData

class GetApiV2HospitalIdResponse(StrictResponseModel):
    data: GetApiV2HospitalIdResponseData

