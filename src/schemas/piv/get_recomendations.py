from typing import Any, List, Optional

from src.schemas.piv.common import StrictResponseModel


class GetRecomendationsAttachment(StrictResponseModel):
    type: Any
    url: Any


class GetRecomendationsItem(StrictResponseModel):
    id: Any
    content: Any
    date: Any
    petName: Any
    petType: Any
    doctorFIO: Any
    media: Optional[Any] = None
    attachments_data: Optional[List[GetRecomendationsAttachment]] = None


class GetRecomendationsData(StrictResponseModel):
    totalCount: Any
    recomendation: List[GetRecomendationsItem]


class GetRecomendationsResponse(StrictResponseModel):
    success: Any
    message: Any
    data: GetRecomendationsData
