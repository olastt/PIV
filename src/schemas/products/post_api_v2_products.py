from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2ProductsResponseDataProductDataSaleParamsGridItem(StrictResponseModel):
    min_price: Any
    price: Any
    max_price: Any
    coefficient: Any
    unit_sale_id: Any
    barcode: Any
    status: Any
    markup: Any
    price_formation: Any

class PostApiV2ProductsResponseDataProductData(StrictResponseModel):
    is_service: Any
    title: Any
    price: Any
    group_id: Any
    unit_storage: Any
    is_for_sale: Any
    code: Any
    barcode: Any
    is_call: Any
    department_id: Any
    sale_params_grid: list[PostApiV2ProductsResponseDataProductDataSaleParamsGridItem]
    id: Any

class PostApiV2ProductsResponseData(StrictResponseModel):
    product_data: PostApiV2ProductsResponseDataProductData

class PostApiV2ProductsResponse(StrictResponseModel):
    message: Any
    data: PostApiV2ProductsResponseData

