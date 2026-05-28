from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersDoctorsItem(StrictResponseModel):
    id: Any
    first_name: Any
    middle_name: Any
    last_name: Any
    is_active: Any
    is_limited: Any
    fio: Any


class GetApiV2UsersDoctorsResponse(RootModel[list[GetApiV2UsersDoctorsItem]]):
    pass

