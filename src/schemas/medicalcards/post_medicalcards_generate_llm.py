from pydantic import StrictBool, StrictStr

from src.schemas.medicalcards.common import StrictResponseModel


class GenerateLlmData(StrictResponseModel):
    text: StrictStr


class GenerateLlmResponse(StrictResponseModel):
    success: StrictBool
    data: GenerateLlmData
