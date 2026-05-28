from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdPetsIdResponseTypeData(StrictResponseModel):
    id: Any
    title: Any
    picture: Any
    type: Any

class GetApiV2ClientsIdPetsIdResponseBreedData(StrictResponseModel):
    id: Any
    title: Any
    pet_type_id: Any

class GetApiV2ClientsIdPetsIdResponse(StrictResponseModel):
    pet_id: Any
    type: Any
    name: Any
    breed: Any
    birthdate: Any
    pet_type_id: Any
    url: Any
    type_data: GetApiV2ClientsIdPetsIdResponseTypeData
    breed_data: GetApiV2ClientsIdPetsIdResponseBreedData
    type_id: Any
    breed_id: Any
    sex: Any
    note: Any
    chip_number: Any
    lab_number: Any
    color_id: Any
    owner_id: Any
    date_register: Any
    deathnote: Any
    deathdate: Optional[Any] = None
    status: Any
    weight: Any

