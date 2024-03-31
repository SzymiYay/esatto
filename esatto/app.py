from .data_loader.json_loader import get_patients_data
from .data_loader.patients_loader import get_patients
from .patient.service import PatientService
from .patient.types import SortCriteria

from .db.model.patient import Patient
from .db.model.address import Address
from .db.repo.connection import MySQLConnectionPoolBuilder
from .db.repo.crud import CrudRepo
from .db.repo.patient import PatientRepo
from .db.repo.address import AddressRepo

from .logger.model import CustomFormatter, MyLogger

from typing import Final

import logging 

def main() -> None:

    connection_pool = MySQLConnectionPoolBuilder().build()

    patient_repo = PatientRepo(connection_pool)
    address_repo = AddressRepo(connection_pool)

    patient_columns = {
        'id': 'integer primary key auto_increment',
        'first_name': 'varchar(20) not null',
        'last_name': 'varchar(20) not null',
        'PESEL': 'varchar(20) not null'
    }

    address_columns = {
        'id': 'integer primary key auto_increment',
        'street': 'varchar(50) not null',
        'city': 'varchar(50) not null',
        'zip_code': 'varchar(6) not null',
        'patient_id': 'integer not null'
    }

    # patient_repo.create_table(patient_columns)
    # address_repo.create_table(address_columns)

    # patient_repo.insert_many([
    #     Patient(first_name='Jan', last_name='Kowalski', PESEL='00000000001'),
    #     Patient(first_name='Anna', last_name='Nowak', PESEL='00000000002'),
    #     Patient(first_name='Piotr', last_name='Kowalczyk', PESEL='00000000003'),
    # ])

    # address_repo.insert_many([
    #     Address(street='Kowalska', city='Warszawa', zip_code='000001', patient_id=1),
    #     Address(street='Nowa', city='Kraków', zip_code='000002', patient_id=2),
    #     Address(street='Kowalska', city='Warszawa', zip_code='000001', patient_id=3)
    # ])


    """LOGGING"""
    logger = MyLogger.get_logger()

    """APP"""
    logger.warning('STARTING APP')
    # FILENAME: Final[str] = 'esatto/data/patients.json'

    # patients_data = get_patients_data(FILENAME)
    # logger.info('Successfully loaded patients data from file')
    # print(patients_data)

    # patients = get_patients(patients_data)
    # logger.info('Successfully created patients')

    # for patient in patients:
    #     print(patient)


    patients = patient_repo.get_all()
    patient_service = PatientService(patients)
    logger.info('Successfully created patient service')

    logger.info('Sorting patients')
    print(patient_service.sort_by(SortCriteria.FIRST_NAME))
    print(patient_service.sort_by(SortCriteria.LAST_NAME))
    print(patient_service.sort_by(SortCriteria.PESEL, reverse=True))

    logger.info('Getting patients by city')
    patients_by_city = patient_service.get_patients_from_every_city(connection_pool)
    print(patients_by_city)

    logger.info('Getting patient by PESEL')
    print(patient_service.get_patient_by_pesel('00000000001'))

    logger.warning('ENDING APP')