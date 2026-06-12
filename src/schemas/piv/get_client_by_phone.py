from typing import Any

from src.schemas.piv.common import StrictResponseModel


class GetClientByPhoneData(StrictResponseModel):
    client_id: Any


class GetClientByPhoneResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetClientByPhoneData
