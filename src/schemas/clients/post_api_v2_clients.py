from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2ClientsResponseDataClientData(StrictResponseModel):
    client_id: Any
    first_name: Any
    last_name: Any
    middle_name: Any

class PostApiV2ClientsResponseData(StrictResponseModel):
    client_data: PostApiV2ClientsResponseDataClientData

class PostApiV2ClientsResponse(StrictResponseModel):
    message: Any
    data: PostApiV2ClientsResponseData

