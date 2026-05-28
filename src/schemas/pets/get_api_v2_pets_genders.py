from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2PetsGendersItem(StrictResponseModel):
    index: Any
    title: Any


class GetApiV2PetsGendersResponse(RootModel[list[GetApiV2PetsGendersItem]]):
    pass

