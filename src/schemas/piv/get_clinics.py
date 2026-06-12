from typing import Any, List, Optional

from src.schemas.piv.common import StrictResponseModel


class GetClinicsCity(StrictResponseModel):
    title: Any


class GetClinicsItem(StrictResponseModel):
    id: Any
    title: Any
    address: Any
    phone: Any
    start_time: Any
    end_time: Any
    city: GetClinicsCity


class GetClinicsData(StrictResponseModel):
    totalCount: Any
    clinics: List[GetClinicsItem]


class GetClinicsResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetClinicsData


class GetClinicsFlatResponse(StrictResponseModel):
    """Альтернативный формат ответа /clinics из Postman-примеров."""
    success: Any
    message: Any
    data: GetClinicsItem
