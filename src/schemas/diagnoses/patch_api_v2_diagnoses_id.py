from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PatchApiV2DiagnosesIdResponseDataDiagnosData(StrictResponseModel):
    id: Any
    title: Any
    status: Any

class PatchApiV2DiagnosesIdResponseData(StrictResponseModel):
    diagnos_data: PatchApiV2DiagnosesIdResponseDataDiagnosData

class PatchApiV2DiagnosesIdResponse(StrictResponseModel):
    message: Any
    data: PatchApiV2DiagnosesIdResponseData

