from typing import Any, List, Optional

from src.schemas.piv.common import StrictResponseModel


class GetDiscountCardItem(StrictResponseModel):
    id: Any
    pet_id: Any
    title: Any
    number: Any
    create_date: Any
    card_type: Any
    is_default: Any
    end_date: Any
    start_date: Any


class GetDiscountCardGroup(StrictResponseModel):
    totalCount: Any
    card: List[GetDiscountCardItem]


class GetDiscountCardData(StrictResponseModel):
    totalCount: Any
    card: List[GetDiscountCardItem]


class GetDiscountCardResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetDiscountCardData


class GetDiscountCardListResponse(StrictResponseModel):
    """Альтернативный формат: data как список групп карт."""
    success: Any
    message: Any
    data: List[GetDiscountCardGroup]
