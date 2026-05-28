from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2CombomanualsReasonsofvisitItem(StrictResponseModel):
    id: Any
    title: Any
    dop_param1: Any
    dop_param2: Any
    color: Any


class GetApiV2CombomanualsReasonsofvisitResponse(RootModel[list[GetApiV2CombomanualsReasonsofvisitItem]]):
    pass

