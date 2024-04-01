from fastapi import HTTPException, status
from fastapi_sqlalchemy import db

from src import models
from src.users import schemas


def deactivate_account(user_id: int):
    db_user = db.session.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db_patients = db.session.query(models.Patient).filter(models.Patient.user_id == user_id).all()

    for db_patient in db_patients:
        db.session.delete(db_patient)

    db_tokens = db.session.query(models.Token).filter(models.Token.user_id == user_id).all()
    for db_token in db_tokens:
        db.session.delete(db_token)
    
    db.session.delete(db_user)
    db.session.commit()


def get_patients(user_id: int):
    db_patients = db.session.query(models.Patient).filter(models.Patient.user_id == user_id).all()
    return db_patients


def get_patient(patient_id: int):
    db_patient = db.session.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")

    return db_patient

def get_patient_by_name(patient_name: str):
    db_patient = db.session.query(models.Patient).filter(models.Patient.first_name == patient_name).first()

    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")

    return db_patient

def create_patient(patient, user_id: int):
    db_patient = models.Patient(first_name=patient.first_name, last_name=patient.last_name, PESEL=patient.PESEL, user_id=user_id, city=patient.city, street=patient.street, zip_code=patient.zip_code)
    db.session.add(db_patient)
    db.session.commit()
    return db_patient


def delete_patient(patient_id: int):
    # db_measurements = db.session.query(models.Measurement).filter(models.Measurement.patient_id == patient_id).all()
    # for db_measurement in db_measurements:
    #     db.session.delete(db_measurement)
        
    db_patient = db.session.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    
    db.session.delete(db_patient)
    db.session.commit()
    return db_patient

def delete_patient_by_name(patient_name: str):
    db_patient = db.session.query(models.Patient).filter(models.Patient.first_name == patient_name).first()

    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    
    db.session.delete(db_patient)
    db.session.commit()
    return db_patient
