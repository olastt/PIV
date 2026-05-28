from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel, StrictBool, StrictFloat, StrictInt, StrictStr


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class GetApiV2UsersIdHomeResponseCallsDataSave(StrictResponseModel):
    data: list[Any]
    total: Any

class GetApiV2UsersIdHomeResponseCallsData(StrictResponseModel):
    save: GetApiV2UsersIdHomeResponseCallsDataSave

class GetApiV2UsersIdHomeResponseAdmissionsDataSave(StrictResponseModel):
    data: list[Any]
    total: Any

class GetApiV2UsersIdHomeResponseAdmissionsDataInTreatment(StrictResponseModel):
    data: list[Any]
    total: Any

class GetApiV2UsersIdHomeResponseAdmissionsDataSaveWithoutDoctor(StrictResponseModel):
    data: list[Any]
    total: Any

class GetApiV2UsersIdHomeResponseAdmissionsDataInTreatmentWithoutDoctor(StrictResponseModel):
    data: list[Any]
    total: Any

class GetApiV2UsersIdHomeResponseAdmissionsDataNotConfirmed(StrictResponseModel):
    total: Any

class GetApiV2UsersIdHomeResponseAdmissionsData(StrictResponseModel):
    save: GetApiV2UsersIdHomeResponseAdmissionsDataSave
    in_treatment: GetApiV2UsersIdHomeResponseAdmissionsDataInTreatment
    save_without_doctor: GetApiV2UsersIdHomeResponseAdmissionsDataSaveWithoutDoctor
    in_treatment_without_doctor: GetApiV2UsersIdHomeResponseAdmissionsDataInTreatmentWithoutDoctor
    not_confirmed: GetApiV2UsersIdHomeResponseAdmissionsDataNotConfirmed

class GetApiV2UsersIdHomeResponseTimesheetData(StrictResponseModel):
    today: Optional[Any] = None
    nextday: Optional[Any] = None
    is_empty_shedules: Any

class GetApiV2UsersIdHomeResponse(StrictResponseModel):
    calls_data: GetApiV2UsersIdHomeResponseCallsData
    admissions_data: GetApiV2UsersIdHomeResponseAdmissionsData
    timesheet_data: GetApiV2UsersIdHomeResponseTimesheetData

