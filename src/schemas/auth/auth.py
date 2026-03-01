from typing import Optional, List
from pydantic import BaseModel, StrictInt, StrictStr, StrictBool


class DiagnosisData(BaseModel):
    id: StrictStr
    type: StrictInt


class PatientData(BaseModel):
    id: StrictInt
    owner_id: StrictInt
    type_id: StrictInt
    alias: StrictStr
    sex: Optional[StrictStr] = None
    date_register: StrictStr
    birthday: Optional[StrictStr] = None
    note: Optional[StrictStr] = None
    breed_id: Optional[StrictInt] = None
    old_id: Optional[StrictInt] = None
    color_id: Optional[StrictInt] = None
    deathnote: Optional[StrictStr] = None
    deathdate: Optional[StrictStr] = None
    chip_number: Optional[StrictStr] = None
    lab_number: Optional[StrictStr] = None
    status: StrictStr
    picture: Optional[StrictStr] = None
    weight: Optional[StrictStr] = None
    edit_date: Optional[StrictStr] = None


class CreateMedcardModel(BaseModel):
    id: StrictInt
    patient_id: StrictInt
    date_create: StrictStr
    date_edit: Optional[StrictStr] = None
    diagnos: Optional[StrictStr] = None
    recomendation: Optional[StrictStr] = None
    invoice: Optional[StrictInt] = None
    admission_type: StrictInt
    weight: Optional[StrictStr] = None
    temperature: Optional[StrictStr] = None
    meet_result_id: Optional[StrictInt] = None
    description: Optional[StrictStr] = None
    next_meet_id: StrictInt
    doctor_id: StrictInt
    creator_id: StrictInt
    status: StrictStr
    calling_id: StrictInt
    admission_id: StrictInt
    diagnos_text: Optional[StrictStr] = None
    diagnos_type_text: Optional[StrictStr] = None
    clinic_id: StrictInt
    patient: PatientData


class MedcardListData(BaseModel):
    totalCount: StrictInt
    medicalCards: List[CreateMedcardModel]


class MedcardPostResponse(BaseModel):
    success: StrictBool
    message: StrictStr
    data: MedcardListData