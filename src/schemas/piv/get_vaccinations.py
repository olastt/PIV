from pydantic import StrictBool, StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetVaccinationsPet(StrictResponseModel):
    type: StrictStr
    alias: StrictStr
    pet_type_title: StrictStr


class GetVaccinationsItem(StrictResponseModel):
    medcard_id: StrictStr
    vaccine_id: StrictStr
    vaccination_date: StrictStr
    date_nexttime: StrictStr
    vaccine_type_title: StrictStr
    name: StrictStr
    pet: GetVaccinationsPet
    type_id: StrictStr
    vaccine_description: dict | None = None


class GetVaccinationsData(StrictResponseModel):
    totalCount: StrictInt
    vaccination: list[list[GetVaccinationsItem]]


class GetVaccinationsResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetVaccinationsData
