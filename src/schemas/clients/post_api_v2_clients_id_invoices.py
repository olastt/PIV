from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2ClientsIdInvoicesResponseDataInvoiceData(StrictResponseModel):
    invoice_id: Any
    amount: Any
    status: Any
    paid_amount: Any

class PostApiV2ClientsIdInvoicesResponseData(StrictResponseModel):
    invoice_data: PostApiV2ClientsIdInvoicesResponseDataInvoiceData

class PostApiV2ClientsIdInvoicesResponse(StrictResponseModel):
    message: Any
    data: PostApiV2ClientsIdInvoicesResponseData

