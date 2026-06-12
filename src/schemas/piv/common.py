from typing import Any, List, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PivErrorData(StrictResponseModel):
    errorCode: Any


class PivErrorResponse(StrictResponseModel):
    success: Any
    message: Any
    data: Optional[PivErrorData] = None


class PivErrorResponseList(RootModel[List[PivErrorResponse]]):
    pass
