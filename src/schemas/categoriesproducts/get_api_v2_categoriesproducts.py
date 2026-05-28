from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2CategoriesproductsResponseDataItem(StrictResponseModel):
    id: Any
    title: Any
    is_double: Any
    sort_priority: Any
    condition_doubling: Any
    status: Any

class GetApiV2CategoriesproductsResponse(StrictResponseModel):
    data: list[GetApiV2CategoriesproductsResponseDataItem]

