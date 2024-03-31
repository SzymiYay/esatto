from dataclasses import dataclass

@dataclass
class Address:
    id: int | None = None
    street: str | None = None
    city: str | None = None
    zip_code: str | None = None
    patient_id: int | None = None