from ..patient.model import Patient
from ..patient.validator import PatientValidator
from typing import Any

def get_patients(patients_data: list[dict[str, Any]]) -> list[Patient]:
    return [Patient.from_dict(patient_data) for patient_data in patients_data if PatientValidator().validate(patient_data)]