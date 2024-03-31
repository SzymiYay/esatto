from .model import Patient

from dataclasses import dataclass

@dataclass
class PatientService:
    patients: list[Patient]