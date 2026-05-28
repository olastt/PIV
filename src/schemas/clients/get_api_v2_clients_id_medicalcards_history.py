from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2ClientsIdMedicalcardsHistoryItemDoctorData(StrictResponseModel):
    doctor_id: Any
    first_name: Any
    last_name: Any
    middle_name: Any

class GetApiV2ClientsIdMedicalcardsHistoryItem(StrictResponseModel):
    medical_card_id: Any
    date: Any
    medical_card_status: Any
    healing_process: Any
    recomendation: Any
    weight: Any
    temperature: Any
    meet_result_title: Any
    admission_type_title: Any
    doctor_data: GetApiV2ClientsIdMedicalcardsHistoryItemDoctorData
    diagnos_data: list[Any]
    styles_content: Any
    styles_content_images: Any
    editable: Any


class GetApiV2ClientsIdMedicalcardsHistoryResponse(RootModel[list[GetApiV2ClientsIdMedicalcardsHistoryItem]]):
    pass

