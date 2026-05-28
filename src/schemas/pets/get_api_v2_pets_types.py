from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2PetsTypesItem(StrictResponseModel):
    id: Any
    title: Any
    type: Any
    url: Any


class GetApiV2PetsTypesResponse(RootModel[list[GetApiV2PetsTypesItem]]):
    pass

