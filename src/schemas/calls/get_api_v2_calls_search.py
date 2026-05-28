from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2CallsSearchItemPet(StrictResponseModel):
    pet_id: Any
    type: Any
    name: Any
    pet_type_title: Any
    url: Any
    pet_type_id: Any

class GetApiV2CallsSearchItemClient(StrictResponseModel):
    client_id: Any
    first_name: Any
    last_name: Any
    cell_phone: Any

class GetApiV2CallsSearchItem(StrictResponseModel):
    call_id: Any
    date: Any
    status: Any
    note: Any
    pet: GetApiV2CallsSearchItemPet
    client: GetApiV2CallsSearchItemClient


class GetApiV2CallsSearchResponse(RootModel[list[GetApiV2CallsSearchItem]]):
    pass

