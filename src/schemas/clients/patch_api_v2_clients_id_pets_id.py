from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PatchApiV2ClientsIdPetsIdResponseDataPetData(StrictResponseModel):
    id: Any
    alias: Any
    pet_type: Any
    pet_type_id: Any
    breed_id: Any
    birthdate: Any
    sex: Any
    color_id: Any
    chip_number: Any
    lab_number: Any
    note: Any
    url: Any

class PatchApiV2ClientsIdPetsIdResponseData(StrictResponseModel):
    pet_data: PatchApiV2ClientsIdPetsIdResponseDataPetData

class PatchApiV2ClientsIdPetsIdResponse(StrictResponseModel):
    message: Any
    data: PatchApiV2ClientsIdPetsIdResponseData

