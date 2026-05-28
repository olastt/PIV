from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdInvoicesItemCreator(StrictResponseModel):
    first_name: Any
    middle_name: Any
    last_name: Any
    nickname: Any
    login: Any
    email: Any
    cell_phone: Any

class GetApiV2ClientsIdInvoicesItemDoctor(StrictResponseModel):
    first_name: Any
    middle_name: Any
    last_name: Any
    nickname: Any
    login: Any
    email: Any
    cell_phone: Any

class GetApiV2ClientsIdInvoicesItemPet(StrictResponseModel):
    pet_id: Any
    owner_id: Any
    alias: Any
    sex: Any
    birthday: Any
    note: Any
    pet_type: Any
    breed: Any

class GetApiV2ClientsIdInvoicesItem(StrictResponseModel):
    id: Any
    status: Any
    discount: Any
    amount: Any
    paid_amount: Any
    date_create: Any
    invoice_date: Any
    creator_id: Any
    creator: GetApiV2ClientsIdInvoicesItemCreator
    doctor: GetApiV2ClientsIdInvoicesItemDoctor
    pet: GetApiV2ClientsIdInvoicesItemPet


class GetApiV2ClientsIdInvoicesResponse(RootModel[list[GetApiV2ClientsIdInvoicesItem]]):
    pass

