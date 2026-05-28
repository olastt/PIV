from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdContactsItem(StrictResponseModel):
    date: Any
    type: Any
    type_desc: Any
    result: Any
    information: Any


class GetApiV2ClientsIdContactsResponse(RootModel[list[GetApiV2ClientsIdContactsItem]]):
    pass

