from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersIdSchedulesResponseDataItem(StrictResponseModel):
    date: Any
    time_start: Any
    time_end: Any
    is_weekend: Any
    interval_type_title: Any

class GetApiV2UsersIdSchedulesResponse(StrictResponseModel):
    data: list[GetApiV2UsersIdSchedulesResponseDataItem]
    is_empty_shedules: Any

