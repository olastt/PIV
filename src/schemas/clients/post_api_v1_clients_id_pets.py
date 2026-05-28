from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV1ClientsIdPetsResponseDataPetData(StrictResponseModel):
    pet_id: Any
    alias: Any

class PostApiV1ClientsIdPetsResponseData(StrictResponseModel):
    pet_data: PostApiV1ClientsIdPetsResponseDataPetData

class PostApiV1ClientsIdPetsResponse(StrictResponseModel):
    message: Any
    data: PostApiV1ClientsIdPetsResponseData

