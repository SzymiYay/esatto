from dataclasses import dataclass

@dataclass
class Patient:
    id: int
    first_name: str | None
    last_name: str | None
    PESEL: str | None