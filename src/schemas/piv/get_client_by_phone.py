from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, StrictBool

from src.schemas.piv.common import StrictResponseModel


class GetClientByPhoneData(StrictResponseModel):
    client_id: StrictInt


class GetClientByPhoneResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetClientByPhoneData
