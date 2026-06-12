from pydantic import StrictBool, StrictStr

from src.schemas.piv.common import StrictResponseModel


class PostSendSmsResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
