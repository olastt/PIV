from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2CombomanualsStreetsResponseDataStreetData(StrictResponseModel):
    title: Any
    city_id: Any
    type: Any
    id: Any

class PostApiV2CombomanualsStreetsResponseData(StrictResponseModel):
    street_data: PostApiV2CombomanualsStreetsResponseDataStreetData

class PostApiV2CombomanualsStreetsResponse(StrictResponseModel):
    message: Any
    data: PostApiV2CombomanualsStreetsResponseData

