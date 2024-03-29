from .data_loader.json_loader import get_patients_data
from .data_loader.patients_loader import get_patients

from .logger.model import CustomFormatter, MyLogger

from typing import Final

import logging 

def main() -> None:

    """LOGGING"""
    logger = MyLogger.get_logger()

    """APP"""
    logger.warning('STARTING APP')
    FILENAME: Final[str] = 'esatto/data/patients.json'

    patients_data = get_patients_data(FILENAME)
    logger.info('Successfully loaded patients data from file')
    print(patients_data)

    patients = get_patients(patients_data)
    logger.info('Successfully created patients')

    for patient in patients:
        print(patient)

    logger.warning('ENDING APP')