from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PatchApiV2ClientsIdResponseDataClientData(StrictResponseModel):
    client_id: Any
    first_name: Any
    last_name: Any
    middle_name: Any
    cell_phone: Any
    note: Any
    status: Any
    phone_prefix: Any

class PatchApiV2ClientsIdResponseData(StrictResponseModel):
    client_data: PatchApiV2ClientsIdResponseDataClientData

class PatchApiV2ClientsIdResponse(StrictResponseModel):
    message: Any
    data: PatchApiV2ClientsIdResponseData

