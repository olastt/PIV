from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2ClientsIdMedicalcardsResponseDataMedicalcardsData(StrictResponseModel):
    medicalcard_id: Any

class PostApiV2ClientsIdMedicalcardsResponseData(StrictResponseModel):
    medicalcards_data: PostApiV2ClientsIdMedicalcardsResponseDataMedicalcardsData

class PostApiV2ClientsIdMedicalcardsResponse(StrictResponseModel):
    message: Any
    data: PostApiV2ClientsIdMedicalcardsResponseData

