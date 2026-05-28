from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2CombomanualsCitiesItem(StrictResponseModel):
    id: Any
    title: Any
    type_id: Any


class GetApiV2CombomanualsCitiesResponse(RootModel[list[GetApiV2CombomanualsCitiesItem]]):
    pass

