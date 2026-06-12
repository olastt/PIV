from pydantic import StrictBool, StrictStr

from src.schemas.piv.common import StrictResponseModel


class PostEventResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
