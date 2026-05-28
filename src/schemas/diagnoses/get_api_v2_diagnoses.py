from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2DiagnosesItem(StrictResponseModel):
    id: Any
    title: Any
    status: Any


class GetApiV2DiagnosesResponse(RootModel[list[GetApiV2DiagnosesItem]]):
    pass

