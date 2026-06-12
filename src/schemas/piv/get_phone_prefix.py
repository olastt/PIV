from typing import Any

from src.schemas.piv.common import StrictResponseModel


class GetPhonePrefixData(StrictResponseModel):
    prefix: Any


class GetPhonePrefixResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetPhonePrefixData
