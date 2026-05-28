from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdPetsItem(StrictResponseModel):
    pet_id: Any
    type: Any
    pet_type_id: Any
    url: Any
    name: Any
    breed: Any
    birthdate: Any
    sex: Any
    note: Any
    date_register: Any


class GetApiV2ClientsIdPetsResponse(RootModel[list[GetApiV2ClientsIdPetsItem]]):
    pass

