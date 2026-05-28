from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2PropertiesResponse(StrictResponseModel):
    unisender_phone_pristavka: Any
    currency_short: Any = Field(alias='currency-short')
    digits_store: Any = Field(alias='digits-store')
    digits_default: Any = Field(alias='digits-default')
    phone_mask: Any
    currency_full: Any = Field(alias='currency-full')
    currency_full_genitive: Any = Field(alias='currency-full-genitive')
    currency_full_many: Any = Field(alias='currency-full-many')
    currency_cent_short: Any = Field(alias='currency-cent-short')
    currency_cent_full: Any = Field(alias='currency-cent-full')
    currency_cent_full_genitive: Any = Field(alias='currency-cent-full-genitive')
    currency_cent_many: Any = Field(alias='currency-cent-many')

