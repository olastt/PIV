from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersIdSettingsPaymentResponse(StrictResponseModel):
    id: Any
    clinic_id: Any
    cassa_id: Any
    user_id: Any

