from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdResponseCityData(StrictResponseModel):
    id: Any
    title: Any
    type_id: Any

class GetApiV2ClientsIdResponse(StrictResponseModel):
    client_id: Any
    first_name: Any
    middle_name: Any
    last_name: Any
    discount: Any
    email: Any
    cell_phone: Any
    address: Any
    type: Any
    in_blacklist: Any
    description: Any
    last_visit_date: Any
    apartment: Any
    city_data: GetApiV2ClientsIdResponseCityData
    street_data: Optional[Any] = None
    balance: Any
    status: Any
    phone_prefix: Any
    clinic_phone_prefix: Any

