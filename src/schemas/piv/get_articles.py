from pydantic import Field, StrictBool, StrictInt, StrictStr

from src.schemas.piv.common import StrictResponseModel


class GetArticlesItem(StrictResponseModel):
    id: StrictInt
    domain: StrictStr
    title: StrictStr
    content: StrictStr
    created_at: StrictStr
    updated_at: StrictStr


class GetArticlesLink(StrictResponseModel):
    url: StrictStr | None
    label: StrictStr
    active: StrictBool


class GetArticlesResponse(StrictResponseModel):
    current_page: StrictInt
    data: list[GetArticlesItem]
    first_page_url: StrictStr
    from_: StrictInt | None = Field(default=None, alias="from")
    last_page: StrictInt
    last_page_url: StrictStr
    links: list[GetArticlesLink]
    next_page_url: StrictStr | None
    path: StrictStr
    per_page: StrictStr
    prev_page_url: StrictStr | None
    to: StrictInt | None
    total: StrictInt
