from dataclasses import dataclass

@dataclass
class Address:
    street: str
    city: str
    zip_code: str

    def __str__(self) -> str:
        return f"""
                Street: {self.street}
                City: {self.city}
                Zip code: {self.zip_code}
                """
    
    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'Address':
        address = Address(**data)
        return address