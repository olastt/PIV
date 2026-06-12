from typing import Any, List

from src.schemas.piv.common import StrictResponseModel


class GetLastThreeArticlesItem(StrictResponseModel):
    id: Any
    domain: Any
    title: Any
    content: Any
    created_at: Any
    updated_at: Any


class GetLastThreeArticlesResponse(StrictResponseModel):
    articles: List[GetLastThreeArticlesItem]
