from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
from ..logger.model import MyLogger

import re

@dataclass
class Validator(ABC):
    errors = None

    @abstractmethod
    def validate(self, data: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    def errors_to_str(self) -> str:
        return f"{', '.join([f'{key}: {message}' for key, message in self.errors.items()])}"

    @staticmethod
    def matches_regex(regex: str, text: str) -> bool:
        return re.match(regex, text) is not None
    
    @staticmethod
    def has_only_upper(text: str) -> bool:
        return Validator.matches_regex(r'^([A-Z]+\s?)+$', text)

class PatientValidator(Validator):

    def __init__(self):
        super().__init__()
    
    def validate(self, patient_data: dict[str, Any]) -> bool:
        self.errors = {
            'first_name': self._validate_first_name(patient_data),
            'last_name': self._validate_last_name(patient_data),
            'PESEL': self._validate_PESEL(patient_data),
            'address': self._validate_address(patient_data)
        }

        logger_validator = MyLogger.get_logger()

        if len(self.errors['first_name']) != 0 or \
           len(self.errors['last_name']) != 0 or \
           len(self.errors['PESEL']) != 0:
            logger_validator.error(', '.join([f'{k}: {v}' for k, v in self.errors.items()]))
            return False

        return True
    
    def _validate_first_name(self, patient_data: dict[str, Any]) -> str:
        if 'first_name' not in patient_data:
            return ['Required']

        errors = []
        patient_first_name = patient_data['first_name']

        if not isinstance(patient_first_name, str):
            errors.append('Must be a string')

        if len(patient_first_name) < 2:
            errors.append('Must be at least 2 characters long')

        if len(patient_first_name) > 50:
            errors.append('Must be at most 50 characters long')

        if not self.matches_regex(r'^[A-Za-z]*$', patient_first_name):
            errors.append('Must contain only letters')

        return errors
    
    def _validate_last_name(self, patient_data: dict[str, Any]) -> str:
        if 'last_name' not in patient_data:
            return ['Required']

        errors = []
        patient_last_name = patient_data['last_name']

        if not isinstance(patient_last_name, str):
            errors.append('Must be a string')

        if len(patient_last_name) < 2:
            errors.append('Must be at least 2 characters long')

        if len(patient_last_name) > 50:
            errors.append('Must be at most 50 characters long')

        if not self.matches_regex(r'^[A-Za-z]*$', patient_last_name):
            errors.append('Must contain only letters')

        return errors
    
    def _validate_PESEL(self, patient_data: dict[str, Any]) -> str:
        if 'PESEL' not in patient_data:
            return ['Required']

        errors = []
        patient_PESEL = patient_data['PESEL']

        if not isinstance(patient_PESEL, str):
            errors.append('Must be a string')

        if len(patient_PESEL) != 11:
            errors.append('Must be 11 characters long')

        if not self.matches_regex(r'^[0-9]*$', patient_PESEL):
            errors.append('Must contain only digits')

        return errors
    
    def _validate_address(self, patient_data: dict[str, Any]) -> str:
        if 'address' not in patient_data:
            return ['Required']

        errors = []
        patient_address = patient_data['address']
        street = patient_address['street']
        city = patient_address['city']
        zip_code = patient_address['zip_code']

        if not isinstance(patient_address, dict):
            errors.append('Must be a dictionary')

        if 'street' not in patient_address:
            errors.append('Street is required')

        if len(street) < 2:
            errors.append('Street must be at least 2 characters long')
        
        if len(street) > 50:
            errors.append('Street must be at most 50 characters long')

        if not self.matches_regex(r'^[A-Za-z0-9]*$', street):
            errors.append('Street must contain only letters and digits')


        if 'city' not in patient_address:
            errors.append('City is required')

        if len(city) < 2:
            errors.append('City must be at least 2 characters long')

        if len(city) > 50:
            errors.append('City must be at most 50 characters long')

        if not self.matches_regex(r'^[A-Za-z]*$', city):
            errors.append('City must contain only letters')


        if 'zip_code' not in patient_address:
            errors.append('Zip code is required')

        if len(zip_code) != 6:
            errors.append('Zip code must be 6 characters long')

        if not self.matches_regex(r'^[0-9]*$', zip_code):
            errors.append('Zip code must contain only digits')


        return errors
