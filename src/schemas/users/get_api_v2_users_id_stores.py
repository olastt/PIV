from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersIdStoresItem(StrictResponseModel):
    id: Any
    title: Any


class GetApiV2UsersIdStoresResponse(RootModel[list[GetApiV2UsersIdStoresItem]]):
    pass

