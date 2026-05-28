from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2CombomanualsIdStreetsItem(StrictResponseModel):
    id: Any
    title: Any
    city_id: Any
    type: Any


class GetApiV2CombomanualsIdStreetsResponse(RootModel[list[GetApiV2CombomanualsIdStreetsItem]]):
    pass

