from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2CombomanualsVaccinationstypesItem(StrictResponseModel):
    id: Any
    title: Any


class GetApiV2CombomanualsVaccinationstypesResponse(RootModel[list[GetApiV2CombomanualsVaccinationstypesItem]]):
    pass

