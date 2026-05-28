from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ProductsItem(StrictResponseModel):
    id: Any
    title: Any
    price: Any
    group: Any
    group_id: Any
    tag_id: Any
    party_accounts: Optional[Any] = None
    party_accounts_count: Any
    default_price: Any
    is_service: Any
    category_id: Any
    category: Any
    barcode: Any
    min_price_percent: Any
    max_price_percent: Any
    min_price: Any
    max_price: Any
    editable: Any
    unit_sale_param_title: Any


class GetApiV2ProductsResponse(RootModel[list[GetApiV2ProductsItem]]):
    pass

