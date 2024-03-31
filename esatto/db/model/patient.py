from dataclasses import dataclass

@dataclass
class Patient:
    id: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    PESEL: str | None = None