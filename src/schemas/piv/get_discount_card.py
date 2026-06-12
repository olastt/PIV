from pydantic import StrictBool, StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetDiscountCardItem(StrictResponseModel):
    id: StrictInt
    pet_id: StrictInt
    title: StrictStr
    number: StrictInt
    create_date: StrictStr
    card_type: StrictStr
    is_default: StrictBool
    end_date: StrictStr
    start_date: StrictStr


class GetDiscountCardGroup(StrictResponseModel):
    totalCount: StrictInt
    card: list[GetDiscountCardItem]


class GetDiscountCardData(StrictResponseModel):
    totalCount: StrictInt
    card: list[GetDiscountCardItem]


class GetDiscountCardResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetDiscountCardData


class GetDiscountCardListResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: list[GetDiscountCardGroup]
