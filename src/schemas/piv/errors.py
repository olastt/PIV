from pydantic import StrictBool, StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class PivErrorData(StrictResponseModel):
    errorCode: StrictInt


class PivErrorResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: PivErrorData


class PivValidation422Response(StrictResponseModel):
    message: StrictStr
    errors: dict[str, list[StrictStr]]


class PivServerErrorMessageResponse(StrictResponseModel):
    message: StrictStr


class PivSmsCheckErrorResponse(StrictResponseModel):
    success: StrictBool
    errorMessage: StrictStr


class TokenUnauthorizedResponse(StrictResponseModel):
    status: StrictInt
    title: StrictStr
    detail: StrictStr
