from pydantic import StrictInt

from src.schemas.medicalcards.common import SaveResponse, StrictResponseModel


class VaccinationData(StrictResponseModel):
    id: StrictInt


class VaccinationMutationData(StrictResponseModel):
    vaccination_data: VaccinationData


class VaccinationMutationResponse(SaveResponse):
    data: VaccinationMutationData
