from pydantic import StrictBool, StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetPhonePrefixData(StrictResponseModel):
    prefix: StrictInt


class GetPhonePrefixResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetPhonePrefixData
