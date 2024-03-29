from dataclasses import dataclass

@dataclass
class Address:
    id: int
    street: str | None
    city: str | None
    zip_code: str | None
    patient_id: int | None