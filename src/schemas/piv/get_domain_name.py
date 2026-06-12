from pydantic import StrictBool, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetDomainNameData(StrictResponseModel):
    domain_name: StrictStr


class GetDomainNameResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetDomainNameData
