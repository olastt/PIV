from pydantic import StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetLastThreeArticlesItem(StrictResponseModel):
    id: StrictInt
    domain: StrictStr
    title: StrictStr
    content: StrictStr
    created_at: StrictStr
    updated_at: StrictStr


class GetLastThreeArticlesResponse(StrictResponseModel):
    articles: list[GetLastThreeArticlesItem]
