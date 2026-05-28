from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersIdResponseCellPhoneData(StrictResponseModel):
    cell_phone: Any
    phone_prefix: Any
    clinic_phone_prefix: Any

class GetApiV2UsersIdResponse(StrictResponseModel):
    first_name: Any
    middle_name: Any
    last_name: Any
    nickname: Any
    login: Any
    email: Any
    cell_phone: Any
    cell_phone_data: GetApiV2UsersIdResponseCellPhoneData

