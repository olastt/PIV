from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PatchApiV2UsersSettingsPaymentIdResponseDataUserConfig(StrictResponseModel):
    id: Any
    user_id: Any
    param_name: Any
    param_value: Any

class PatchApiV2UsersSettingsPaymentIdResponseData(StrictResponseModel):
    user_config: PatchApiV2UsersSettingsPaymentIdResponseDataUserConfig

class PatchApiV2UsersSettingsPaymentIdResponse(StrictResponseModel):
    message: Any
    data: PatchApiV2UsersSettingsPaymentIdResponseData

