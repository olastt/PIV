from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2CassaIdItem(StrictResponseModel):
    id: Any
    title: Any
    user_id: Any
    suma: Any
    summa_cash: Any
    summa_cashless: Any
    main_cassa: Any


class GetApiV2CassaIdResponse(RootModel[list[GetApiV2CassaIdItem]]):
    pass

