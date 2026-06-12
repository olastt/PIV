from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersIdAdmissionItemPetData(StrictResponseModel):
    pet_id: Any
    sex: Any
    alias: Any
    pet_type: Any
    pet_breed: Any
    birthday: Any
    pet_type_id: Any
    url: Any

class GetApiV2UsersIdAdmissionItemClientData(StrictResponseModel):
    client_id: Any
    first_name: Any
    middle_name: Any
    last_name: Any
    email: Any
    cell_phone: Any
    address: Any
    in_blacklist: Any
    client_type: Any
    phone_prefix: Any
    cell_phone_clean: Any

class GetApiV2UsersIdAdmissionItemDoctorData(StrictResponseModel):
    doctor_id: Any
    last_name: Any
    first_name: Any
    middle_name: Any
    nickname: Any

class GetApiV2UsersIdAdmissionItem(StrictResponseModel):
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
    icon_reception_write_channel: Any
    wait_time: Any
    pet_data: Optional[GetApiV2UsersIdAdmissionItemPetData] = None
    client_data: GetApiV2UsersIdAdmissionItemClientData
    invoices_data: Optional[Any] = None
    doctor_data: GetApiV2UsersIdAdmissionItemDoctorData
    admission_type_color: Optional[Any] = None


class GetApiV2UsersIdAdmissionResponse(RootModel[list[GetApiV2UsersIdAdmissionItem]]):
    pass

