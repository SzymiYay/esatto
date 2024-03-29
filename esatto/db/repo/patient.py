from .crud import CrudRepo
from ..model.patient import Patient


class PatientRepo(CrudRepo):
    def __init__(self, connection_pool):
        super().__init__(connection_pool, Patient)