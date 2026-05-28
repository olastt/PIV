from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdInvoicesIdProductsItemProduct(StrictResponseModel):
    id: Any
    title: Any
    price: Any
    barcode: Any
    category: Any
    group: Any
    tag_id: Any
    group_id: Any
    category_id: Optional[Any] = None
    min_price: Any
    max_price: Any
    min_price_percent: Any
    max_price_percent: Any

class GetApiV2ClientsIdInvoicesIdProductsItem(StrictResponseModel):
    quantity: Any
    price: Any
    product: GetApiV2ClientsIdInvoicesIdProductsItemProduct


class GetApiV2ClientsIdInvoicesIdProductsResponse(RootModel[list[GetApiV2ClientsIdInvoicesIdProductsItem]]):
    pass

