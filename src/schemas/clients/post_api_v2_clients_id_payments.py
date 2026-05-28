from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PostApiV2ClientsIdPaymentsResponseDataInvoiceData(StrictResponseModel):
    invoice_id: Any
    amount: Any

class PostApiV2ClientsIdPaymentsResponseData(StrictResponseModel):
    invoice_data: PostApiV2ClientsIdPaymentsResponseDataInvoiceData

class PostApiV2ClientsIdPaymentsResponse(StrictResponseModel):
    message: Any
    data: PostApiV2ClientsIdPaymentsResponseData

