from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PatchApiV2CategoriesproductsIdResponseDataCategoryData(StrictResponseModel):
    id: Any
    title: Any
    is_double: Any
    sort_priority: Any
    condition_doubling: Any
    status: Any

class PatchApiV2CategoriesproductsIdResponseData(StrictResponseModel):
    category_data: PatchApiV2CategoriesproductsIdResponseDataCategoryData

class PatchApiV2CategoriesproductsIdResponse(StrictResponseModel):
    message: Any
    data: PatchApiV2CategoriesproductsIdResponseData

