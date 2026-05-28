from pydantic import StrictStr

from src.schemas.medicalcards.common import SaveResponse, StrictResponseModel


class CreatedMedicalcardData(StrictResponseModel):
    medicalcard_id: StrictStr


class CreateMedicalcardData(StrictResponseModel):
    medicalcards_data: CreatedMedicalcardData


class CreateMedicalcardResponse(SaveResponse):
    data: CreateMedicalcardData
