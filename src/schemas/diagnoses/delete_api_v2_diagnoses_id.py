from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class DeleteApiV2DiagnosesIdResponseData(StrictResponseModel):
    id: Any

class DeleteApiV2DiagnosesIdResponse(StrictResponseModel):
    message: Any
    data: DeleteApiV2DiagnosesIdResponseData

