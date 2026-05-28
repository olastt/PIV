from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV1CombomanualsResultofvisitItem(StrictResponseModel):
    id: Any
    title: Any


class GetApiV1CombomanualsResultofvisitResponse(RootModel[list[GetApiV1CombomanualsResultofvisitItem]]):
    pass

