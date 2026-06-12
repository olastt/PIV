from pydantic import StrictBool, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetSmsCheckResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
