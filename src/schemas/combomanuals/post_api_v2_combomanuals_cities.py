from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2CombomanualsCitiesResponseDataCityData(StrictResponseModel):
    type_id: Any
    title: Any
    id: Any

class PostApiV2CombomanualsCitiesResponseData(StrictResponseModel):
    city_data: PostApiV2CombomanualsCitiesResponseDataCityData

class PostApiV2CombomanualsCitiesResponse(StrictResponseModel):
    message: Any
    data: PostApiV2CombomanualsCitiesResponseData

