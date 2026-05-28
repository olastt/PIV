from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClinicsItem(StrictResponseModel):
    id: Any
    title: Any
    address: Any
    phone: Any
    city_id: Any
    start_time: Any
    end_time: Any
    internet_address: Any
    guest_client_id: Any
    time_zone: Any


class GetApiV2ClinicsResponse(RootModel[list[GetApiV2ClinicsItem]]):
    pass

