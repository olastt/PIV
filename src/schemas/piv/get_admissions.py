from typing import Any, List, Optional

from src.schemas.piv.common import StrictResponseModel


class GetAdmissionsPet(StrictResponseModel):
    type: Any
    alias: Any
    pet_type_title: Any


class GetAdmissionsItem(StrictResponseModel):
    admission_id: Any
    admission_date: Any
    status: Any
    title_type: Any
    pet: GetAdmissionsPet
    doctorFIO: Any
    description: Any


class GetAdmissionsData(StrictResponseModel):
    totalCount: Any
    admission: List[GetAdmissionsItem]


class GetAdmissionsResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetAdmissionsData
