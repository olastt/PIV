from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, StrictBool

from src.schemas.piv.common import StrictResponseModel


class GetApiKeyByClinicCodeData(StrictResponseModel):
    apiKey: StrictStr


class GetApiKeyByClinicCodeResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetApiKeyByClinicCodeData
