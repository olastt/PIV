from typing import Any, Optional

from src.schemas.piv.common import StrictResponseModel


class PostEventResponse(StrictResponseModel):
    success: Any
    message: Any
    data: Optional[Any] = None
