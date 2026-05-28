from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2HospitalBlocksItem(StrictResponseModel):
    id: Any
    title: Any
    places_count: Any
    reserved_places_count: Any
    is_daily_payment: Any
    is_hourly_payment: Any
    status: Any
    clinic_id: Any


class GetApiV2HospitalBlocksResponse(RootModel[list[GetApiV2HospitalBlocksItem]]):
    pass

