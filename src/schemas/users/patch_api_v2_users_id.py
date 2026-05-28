from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PatchApiV2UsersIdResponseUserData(StrictResponseModel):
    nickname: Any

class PatchApiV2UsersIdResponse(StrictResponseModel):
    error: Any
    message: Any
    user_data: PatchApiV2UsersIdResponseUserData

