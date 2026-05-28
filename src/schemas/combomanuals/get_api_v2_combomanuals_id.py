from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2CombomanualsIdItem(StrictResponseModel):
    id: Any
    combo_manual_id: Any
    title: Any
    value: Any
    dop_param1: Any
    dop_param2: Any
    dop_param3: Any


class GetApiV2CombomanualsIdResponse(RootModel[list[GetApiV2CombomanualsIdItem]]):
    pass

