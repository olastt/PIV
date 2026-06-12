from typing import Any, List, Optional

from pydantic import Field

from src.schemas.piv.common import StrictResponseModel


class GetArticlesLink(StrictResponseModel):
    url: Any
    label: Any
    active: Any


class GetArticlesItem(StrictResponseModel):
    id: Any
    domain: Any
    title: Any
    content: Any
    created_at: Any
    updated_at: Any


class GetArticlesResponse(StrictResponseModel):
    current_page: Any
    data: List[GetArticlesItem]
    first_page_url: Any
    from_: Optional[Any] = Field(default=None, alias="from")
    last_page: Any
    last_page_url: Any
    links: List[GetArticlesLink]
    next_page_url: Any
    path: Any
    per_page: Any
    prev_page_url: Any
    to: Any
    total: Any
