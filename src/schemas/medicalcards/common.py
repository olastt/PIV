from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class DoctorData(StrictResponseModel):
    doctor_id: StrictInt
    doctor_nickname: StrictStr
    first_name: StrictStr
    last_name: StrictStr
    middle_name: StrictStr


class PetData(StrictResponseModel):
    pet_id: StrictInt
    alias: StrictStr
    birthday: Optional[StrictStr] = None
    sex: Optional[StrictStr] = None
    note: Optional[StrictStr] = None
    pet_type: StrictStr
    breed: StrictStr


class ClientData(StrictResponseModel):
    client_id: StrictInt
    first_name: StrictStr
    last_name: StrictStr
    middle_name: StrictStr
    phone: StrictStr


class AdmissionData(StrictResponseModel):
    id: StrictInt
    admission_date: StrictStr
    description: StrictStr
    client_id: StrictInt
    patient_id: StrictInt
    user_id: StrictInt
    type_id: StrictInt
    admission_length: StrictStr
    status: StrictStr
    clinic_id: StrictInt
    direct_direction: StrictInt
    creator_id: StrictInt
    create_date: StrictStr
    escorter_id: StrictInt
    reception_write_channel: StrictStr
    is_auto_create: StrictInt
    invoices_sum: StrictStr
    confirmation: StrictStr
    wait_time: StrictStr
    icon_reception_write_channel: StrictStr


class SaveResponse(StrictResponseModel):
    message: StrictStr


class ErrorTraceItem(StrictResponseModel):
    file: StrictStr
    line: StrictInt
    function: StrictStr
    class_: Optional[StrictStr] = Field(default=None, alias="class")
    type: Optional[StrictStr] = None


class ErrorBody(StrictResponseModel):
    status: StrictInt
    message: StrictStr
    validation_errors: Optional[dict[StrictStr, list[StrictStr]]] = None
    detail: StrictStr
    trace: list[ErrorTraceItem]


class ErrorResponse(StrictResponseModel):
    errors: ErrorBody
