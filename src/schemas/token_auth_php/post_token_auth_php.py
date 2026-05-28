from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostTokenAuthPhpResponseData(StrictResponseModel):
    service: Any
    token: Any
    user_id: Any

class PostTokenAuthPhpResponse(StrictResponseModel):
    status: Any
    title: Any
    detail: Any
    data: PostTokenAuthPhpResponseData

