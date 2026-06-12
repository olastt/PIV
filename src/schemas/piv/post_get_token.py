from typing import Any

from pydantic import BaseModel, ConfigDict


class GetTokenData(BaseModel):
    model_config = ConfigDict(extra="allow")

    service: Any
    token: Any
    user_id: Any


class GetTokenResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    status: Any
    title: Any
    detail: Any
    data: GetTokenData
