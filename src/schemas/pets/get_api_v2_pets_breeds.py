from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2PetsBreedsItem(StrictResponseModel):
    id: Any
    title: Any
    pet_type_id: Any


class GetApiV2PetsBreedsResponse(RootModel[list[GetApiV2PetsBreedsItem]]):
    pass

