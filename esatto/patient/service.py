from .model import Patient
from .types import SortCriteria

from ..db.repo.address import AddressRepo

from dataclasses import dataclass

@dataclass
class PatientsService:
    patients: list[Patient]

    def sort_by(self, sort_criteria: SortCriteria, *, reverse=False) -> list[Patient]:
        match sort_criteria:
            case SortCriteria.FIRST_NAME:
                return sorted(self.patients, key=lambda patient: patient.first_name, reverse=reverse)
            case SortCriteria.LAST_NAME:
                return sorted(self.patients, key=lambda patient: patient.last_name, reverse=reverse)
            case SortCriteria.PESEL:
                return sorted(self.patients, key=lambda patient: int(patient.PESEL), reverse=reverse)
            case _:
                raise ValueError('Invalid sort criteria')
            
    def get_patients_from_every_city(self, connection_pool) -> dict[str, list[Patient]]:
        address_repo = AddressRepo(connection_pool)
        addresses = address_repo.get_all()
        patients_by_city = {}
        for address in addresses:
            patient = next(patient for patient in self.patients if patient.id == address.patient_id)
            patients_by_city.setdefault(address.city, []).append(patient)
        return patients_by_city
    
    def get_patient_by_pesel(self, pesel: str) -> Patient:
        return next(patient for patient in self.patients if patient.PESEL == pesel)
        

    def __str__(self) -> str:
        return f'Patients: {[patient.first_name for patient in self.patients]}'