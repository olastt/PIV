from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2UsersSettingsPaymentIdResponseDataUserConfig(StrictResponseModel):
    id: Any
    user_id: Any
    param_name: Any
    param_value: Any

class PostApiV2UsersSettingsPaymentIdResponseData(StrictResponseModel):
    user_config: PostApiV2UsersSettingsPaymentIdResponseDataUserConfig

class PostApiV2UsersSettingsPaymentIdResponse(StrictResponseModel):
    message: Any
    data: PostApiV2UsersSettingsPaymentIdResponseData

