from typing import TypeAlias

from pydantic import StrictStr

from src.schemas.medicalcards.common import StrictResponseModel


class MedicalcardDiagnosis(StrictResponseModel):
    id: StrictStr
    title: StrictStr


GetMedicalcardsDiagnosesResponse: TypeAlias = list[MedicalcardDiagnosis]
