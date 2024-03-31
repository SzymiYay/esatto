from esatto.patient.service import PatientsService
from esatto.patient.model import Patient
from esatto.patient.types import SortCriteria

from decimal import Decimal

import pytest
import unittest


class TestService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.cars = PatientsService(
            [
                Patient(
                    first_name='John',
                    last_name='Doe',
                    PESEL='00000000001',
                    address={'city': 'Krakow', 'street': 'Krakowska', 'zip_code': '100001'}
                ),
                Patient(
                    first_name='Jane',
                    last_name='Brown',
                    PESEL='00000000002',
                    address={'city': 'Warszawa', 'street': 'Dluga', 'zip_code': '100001'}
                )
            ]
        )

    def test_sorted_by_first_name(self):
        expected_result = [
            Patient(
                first_name='Jane',
                last_name='Brown',
                PESEL='00000000002',
                address={'city': 'Warszawa', 'street': 'Dluga', 'zip_code': '100001'}
            ),
            Patient(
                first_name='John',
                last_name='Doe',
                PESEL='00000000001',
                address={'city': 'Krakow', 'street': 'Krakowska', 'zip_code': '100001'}
            )
        ]
        result = self.cars.sort_by(SortCriteria.FIRST_NAME)
        self.assertListEqual(result, expected_result)

    def test_sorted_by_last_name(self):
        expected_result = [
            Patient(
                first_name='Jane',
                last_name='Brown',
                PESEL='00000000002',
                address={'city': 'Warszawa', 'street': 'Dluga', 'zip_code': '100001'}
            ),
            Patient(
                first_name='John',
                last_name='Doe',
                PESEL='00000000001',
                address={'city': 'Krakow', 'street': 'Krakowska', 'zip_code': '100001'}
            )
        ]
        result = self.cars.sort_by(SortCriteria.LAST_NAME)
        self.assertListEqual(result, expected_result)

    def test_sorted_by_pesel(self):
        expected_result = [
            Patient(
                first_name='Jane',
                last_name='Brown',
                PESEL='00000000002',
                address={'city': 'Warszawa', 'street': 'Dluga', 'zip_code': '100001'}
            ),
            Patient(
                first_name='John',
                last_name='Doe',
                PESEL='00000000001',
                address={'city': 'Krakow', 'street': 'Krakowska', 'zip_code': '100001'}
            )
        ]
        result = self.cars.sort_by(SortCriteria.PESEL, reverse=True)
        self.assertListEqual(result, expected_result)
