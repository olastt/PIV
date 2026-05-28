from pydantic import StrictInt, StrictStr

from src.schemas.medicalcards.common import StrictResponseModel


class VaccinationByPetItem(StrictResponseModel):
    id: StrictInt
    date: StrictStr
    birthday: StrictStr
    title: StrictStr
    doza: StrictInt
    vaccine_type: StrictInt
    vaccine_description: StrictStr
    next_date: StrictStr
    next_time: StrictStr
    vaccine_id: StrictStr
    pet_age_at_time_vaccination: StrictStr


GetVaccinationsByPetResponse = list[VaccinationByPetItem]
