from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2NotificationSettingsResponseData(StrictResponseModel):
    change_doctor_schedule: Any
    new_pending_admissins: Any
    reminder_of_calling: Any
    register_new_client: Any
    end_of_tariff_plan: Any
    create_admissin: Any
    admissin_change: Any
    confirmation_admission: Any

class GetApiV2NotificationSettingsResponse(StrictResponseModel):
    data: GetApiV2NotificationSettingsResponseData

