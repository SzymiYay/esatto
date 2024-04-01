from fastapi import Depends, status, APIRouter
from base64 import b64encode, b64decode
from hashlib import sha256
from time import time
from urllib import parse
from hmac import HMAC
import uuid

from src.users import schemas as user_schema

from src.utils import jwt_util
from src.users import crud as user_crud

from src.logger import logger

router = APIRouter(
    prefix="/api/v1",
    tags=["Users"]
)

@router.get("/users/profile", 
         response_model=user_schema.User, 
         tags=["Users"],
         status_code=status.HTTP_200_OK,
         response_description="User details")
async def get_user_profile(current_user: user_schema.User = Depends(jwt_util.get_current_active_user)):
    return current_user


@router.delete("/users",
            tags=["Users"],
            status_code=status.HTTP_200_OK,
            response_description="User deleted successfully")
async def deactivate_account(current_user: user_schema.User = Depends(jwt_util.get_current_active_user)):
    user_crud.deactivate_account(current_user.id)
    return {"message": "User account deactivated successfully"}


@router.get("/users/patients", 
         response_model=list[user_schema.PatientReturn], 
         tags=["Users"],
         status_code=status.HTTP_200_OK,
         response_description="User patients")
async def get_patients(current_user: user_schema.User = Depends(jwt_util.get_current_active_user)):
    db_patients = user_crud.get_patients(current_user.id)
    return db_patients


@router.post("/users/patients", 
          tags=["Users"],
          status_code=status.HTTP_201_CREATED,
          response_description="Patient created successfully")
async def create_patient(patient: user_schema.Patient, current_user: user_schema.User = Depends(jwt_util.get_current_active_user)):
    patient = user_crud.create_patient(patient, current_user.id)
    return {"message": "Patient created successfully"}


@router.delete("/users/patients/{patient_id}", 
            tags=["Users"],
            status_code=status.HTTP_200_OK,
            response_description="Patient deleted successfully")
async def delete_patient(patient_id, current_user: user_schema.User = Depends(jwt_util.get_current_active_user)):
    db_patient = user_crud.delete_patient(patient_id)
    return {"message": "Patient deleted successfully"}
