from pydantic import StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetTokenData(StrictResponseModel):
    service: StrictStr
    token: StrictStr
    user_id: StrictStr


class GetTokenResponse(StrictResponseModel):
    status: StrictInt
    title: StrictStr
    detail: StrictStr
    data: GetTokenData
