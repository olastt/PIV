from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2CategoriesproductsResponseDataCategoryData(StrictResponseModel):
    is_double: Any
    sort_priority: Any
    condition_doubling: Any
    status: Any
    title: Any
    id: Any

class PostApiV2CategoriesproductsResponseData(StrictResponseModel):
    category_data: PostApiV2CategoriesproductsResponseDataCategoryData

class PostApiV2CategoriesproductsResponse(StrictResponseModel):
    message: Any
    data: PostApiV2CategoriesproductsResponseData

