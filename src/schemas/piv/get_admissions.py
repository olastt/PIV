from pydantic import StrictBool, StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetAdmissionsPet(StrictResponseModel):
    type: StrictStr
    alias: StrictStr
    pet_type_title: StrictStr


class GetAdmissionsItem(StrictResponseModel):
    admission_id: StrictStr
    admission_date: StrictStr
    status: StrictStr
    title_type: StrictStr
    pet: GetAdmissionsPet
    doctorFIO: StrictStr
    description: StrictStr


class GetAdmissionsData(StrictResponseModel):
    totalCount: StrictInt
    admission: list[GetAdmissionsItem]


class GetAdmissionsResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetAdmissionsData
