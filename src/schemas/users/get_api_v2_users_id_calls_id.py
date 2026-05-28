from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersIdCallsIdResponsePet(StrictResponseModel):
    pet_id: Any
    type: Any
    name: Any
    pet_type_title: Any
    url: Any
    pet_type_id: Any

class GetApiV2UsersIdCallsIdResponseClient(StrictResponseModel):
    client_id: Any
    first_name: Any
    last_name: Any
    cell_phone: Any

class GetApiV2UsersIdCallsIdResponse(StrictResponseModel):
    call_id: Any
    date: Any
    status: Any
    note: Any
    pet: GetApiV2UsersIdCallsIdResponsePet
    client: GetApiV2UsersIdCallsIdResponseClient

