from pydantic import BaseModel, ConfigDict


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True, strict=True)
