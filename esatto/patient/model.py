from dataclasses import dataclass
from typing import Any

@dataclass
class Patient:
    first_name: str
    last_name: str
    PESEL: str
    address: Address

    def __str__(self) -> str:
        return f"""
                First name: {self.first_name}
                Last name: {self.last_name}
                PESEL: {self.PESEL}
                Address: {self.address}
                """
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> 'Patient':
        patient = Patient(**data)
        return patient