from typing import Any

from src.schemas.piv.common import StrictResponseModel


class GetDomainNameData(StrictResponseModel):
    domain_name: Any


class GetDomainNameResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetDomainNameData
