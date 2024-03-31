from decimal import Decimal

from esatto.patient.model import Patient
from esatto.data_loader.patients_loader import get_patients

import pytest
import unittest


class TestPatientsLoader(unittest.TestCase):

    def setUp(self) -> None:
        self.patients = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "PESEL": "00000000001",
                "address": {
                    "street": "Krakowska",
                    "city": "Krakow",
                    "zip_code": "100001"
                }
            },
            {
                "first_name": "Jane",
                "last_name": "Brown",
                "PESEL": "00000000002",
                "address": {
                    "street": "Dluga",
                    "city": "Warszawa",
                    "zip_code": "100001"
                }
            }
        ]

    def test_get_patients(self):
        expected_result = [
            Patient(
                first_name='John',
                last_name='Doe',
                PESEL='00000000001',
                address={'city': 'Krakow',
                         'street': 'Krakowska',
                         'zip_code': '100001'}
                ),
            Patient(
                first_name='Jane',
                last_name='Brown',
                PESEL='00000000002',
                address={'city': 'Warszawa', 'street': 'Dluga', 'zip_code': '100001'}
            )]
        result = get_patients(self.patients)

        self.assertListEqual(result, expected_result)
        self.assertIsInstance(result[0], Patient)
        self.assertIsInstance(result[0].PESEL, str)
        self.assertIsInstance(result[0].first_name, str)
        self.assertIsInstance(result[0].last_name, str)
        self.assertIsInstance(result[0].address['city'], str)
        self.assertIsInstance(result[0].address['street'], str)
        self.assertIsInstance(result[0].address['zip_code'], str)
        self.assertIsInstance(result[1], Patient)
        self.assertIsInstance(result[1].PESEL, str)
        self.assertIsInstance(result[1].first_name, str)
        self.assertIsInstance(result[1].last_name, str)
        self.assertIsInstance(result[1].address['city'], str)
        self.assertIsInstance(result[1].address['street'], str)
        self.assertIsInstance(result[1].address['zip_code'], str)

        self.assertEqual(result[0].PESEL, '00000000001')
        self.assertEqual(result[0].first_name, 'John')
        self.assertEqual(result[0].last_name, 'Doe')
        self.assertEqual(result[0].address['city'], 'Krakow')
        self.assertEqual(result[0].address['street'], 'Krakowska')
        self.assertEqual(result[0].address['zip_code'], '100001')
        self.assertEqual(result[1].PESEL, '00000000002')
        self.assertEqual(result[1].first_name, 'Jane')
        self.assertEqual(result[1].last_name, 'Brown')
        self.assertEqual(result[1].address['city'], 'Warszawa')
        self.assertEqual(result[1].address['street'], 'Dluga')
        self.assertEqual(result[1].address['zip_code'], '100001')


if __name__ == '__main__':
    unittest.main()