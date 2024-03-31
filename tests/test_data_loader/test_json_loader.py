from esatto.data_loader.json_loader import get_patients_data


import unittest
import json


class TestJSONLoader(unittest.TestCase):

    def test_get_cars_data(self):
        expected_result = [{'PESEL': '00000000001',
            'address': {'city': 'Krakow', 'street': 'Krakowska', 'zip_code': '100001'},
            'first_name': 'John',
            'last_name': 'Doe'},
        {'PESEL': '00000000002',
            'address': {'city': 'Warszawa', 'street': 'Dluga', 'zip_code': '100001'},
            'first_name': 'Jane',
            'last_name': 'Brown'},
        {'PESEL': '00000000003',
            'address': {'city': 'Poznan', 'street': 'Wielka', 'zip_code': '100001'},
            'first_name': 'Alice',
            'last_name': 'Smith'}]
        result = get_patients_data('esatto/data/patients.json')

        self.assertListEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()