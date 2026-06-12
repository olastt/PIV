from pydantic import StrictBool, StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetClinicsCity(StrictResponseModel):
    title: StrictStr


class GetClinicsItem(StrictResponseModel):
    id: StrictStr
    title: StrictStr
    address: StrictStr
    phone: StrictStr
    start_time: StrictStr
    end_time: StrictStr
    city: GetClinicsCity


class GetClinicsData(StrictResponseModel):
    totalCount: StrictInt
    clinics: list[GetClinicsItem]


class GetClinicsResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetClinicsData


class GetClinicsFlatResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetClinicsItem
