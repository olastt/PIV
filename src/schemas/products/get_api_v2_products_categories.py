from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ProductsCategoriesResponseDataItem(StrictResponseModel):
    id: Any
    title: Any
    is_service: Any

class GetApiV2ProductsCategoriesResponse(StrictResponseModel):
    data: list[GetApiV2ProductsCategoriesResponseDataItem]

