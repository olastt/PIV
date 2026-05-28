from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2UsersIdAdmissionResponseDataAdmissionData(StrictResponseModel):
    admission_id: Any

class PostApiV2UsersIdAdmissionResponseData(StrictResponseModel):
    admission_data: PostApiV2UsersIdAdmissionResponseDataAdmissionData

class PostApiV2UsersIdAdmissionResponse(StrictResponseModel):
    error: Any
    message: Any
    data: PostApiV2UsersIdAdmissionResponseData

