from typing import Any, List, Optional

from src.schemas.piv.common import StrictResponseModel


class GetVaccinationsPet(StrictResponseModel):
    type: Any
    alias: Any
    pet_type_title: Any


class GetVaccinationsItem(StrictResponseModel):
    medcard_id: Any
    vaccine_id: Any
    vaccination_date: Any
    date_nexttime: Any
    vaccine_type_title: Any
    name: Any
    pet: GetVaccinationsPet
    type_id: Any
    vaccine_description: Optional[Any] = None


class GetVaccinationsData(StrictResponseModel):
    totalCount: Any
    # API возвращает массив групп: [[{...}], [{...}]]
    vaccination: List[List[GetVaccinationsItem]]


class GetVaccinationsResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetVaccinationsData
