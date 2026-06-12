from pydantic import Field, StrictBool, StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetRecomendationsAttachment(StrictResponseModel):
    type: StrictStr
    url: StrictStr


class GetRecomendationsItem(StrictResponseModel):
    id: StrictStr
    content: StrictStr
    date: StrictStr
    petName: StrictStr
    petType: StrictStr
    doctorFIO: StrictStr
    media: list = Field(default_factory=list)
    attachments_data: list[GetRecomendationsAttachment] | None = None


class GetRecomendationsData(StrictResponseModel):
    totalCount: StrictInt
    recomendation: list[GetRecomendationsItem]


class GetRecomendationsResponse(StrictResponseModel):
    success: StrictBool
    message: StrictStr
    data: GetRecomendationsData
