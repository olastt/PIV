from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersAdmissionIdResponseClientData(StrictResponseModel):
    client_id: Any
    first_name: Any
    middle_name: Any
    last_name: Any
    email: Any
    cell_phone: Any
    address: Any
    in_blacklist: Any
    unisender_phone_pristavka: Any
    client_type: Any
    phone_prefix: Any
    cell_phone_clean: Any

class GetApiV2UsersAdmissionIdResponse(StrictResponseModel):
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
    wait_time: Optional[Any] = None
    pet_data: Optional[Any] = None
    client_data: GetApiV2UsersAdmissionIdResponseClientData
    invoices_data: Optional[Any] = None

