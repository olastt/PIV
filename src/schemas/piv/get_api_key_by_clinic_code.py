from typing import Any, List, Optional

from src.schemas.piv.common import StrictResponseModel


class GetApiKeyByClinicCodeData(StrictResponseModel):
    apiKey: Any


class GetApiKeyByClinicCodeResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetApiKeyByClinicCodeData
