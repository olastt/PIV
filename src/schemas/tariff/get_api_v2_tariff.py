from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2TariffResponseData(StrictResponseModel):
    name: Any
    is_free: Any
    valid_untill: Any
    users_allowed: Any
    last_paid_period: Any
    prolongation_type: Any
    prolongation_users: Any
    prolongation_period: Any
    date_register: Any
    blocked: Any
    billing_data: Any
    tariff_addons: Any

class GetApiV2TariffResponse(StrictResponseModel):
    data: GetApiV2TariffResponseData

