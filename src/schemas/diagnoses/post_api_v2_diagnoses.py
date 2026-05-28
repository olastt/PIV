from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2DiagnosesResponseDataDiagnosData(StrictResponseModel):
    title: Any
    status: Any
    id: Any

class PostApiV2DiagnosesResponseData(StrictResponseModel):
    diagnos_data: PostApiV2DiagnosesResponseDataDiagnosData

class PostApiV2DiagnosesResponse(StrictResponseModel):
    message: Any
    data: PostApiV2DiagnosesResponseData

