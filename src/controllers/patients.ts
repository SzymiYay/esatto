import express from 'express';
import { getReasonPhrase } from 'http-status-codes';

import { createPatient, deletePatientById, getPatientById, getPatientByName, getPatients } from '../db/patients';
import { getUserBySessionToken, updatePatients } from '../db/users';

export const getAllPatients = async (req: express.Request, res: express.Response) => {
    try {
        const patients = await getPatients();

        return res.status(200).json({
            message: 'Patients fetched successfully',
            data: patients,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        });
    }
}

export const getPatient = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;

        const patient = await getPatientById(id);

        return res.status(200).json({
            message: 'Patient fetched successfully',
            data: patient,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        });
    }
}

export const registerPatient = async (req: express.Request, res: express.Response) => {
    try {
        const { first_name, last_name, PESEL, address } = req.body;
        const user = await getUserBySessionToken(req.cookies.token).lean();
        const userId = user._id.toString();

        if (!first_name || !last_name || !PESEL || !address) {
            return res.status(400).json({
                message: 'Missing required fields in patient registration',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const existingPatient = await getPatientByName(first_name);

        if (existingPatient) {
            return res.status(400).json({
                message: 'Patient already exists',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const patient: any = await createPatient({
            first_name,
            last_name,
            PESEL, 
            address,
        });

        await updatePatients(userId, { patientId: patient._id });

        return res.status(200).json({
            message: 'Patient registered successfully',
            data: patient,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        });
    }
}

export const deletePatient = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;

        const deletedPatient = await deletePatientById(id);

        return res.json({
            message: 'Patient deleted successfully',
            data: deletedPatient,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        });
    }
}

export const updatePatient = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;
        const { first_name, last_name, PESEL, address } = req.body;

        if (!first_name || !last_name || !PESEL) {
            return res.status(400).json({
                message: 'Missing required fields in patient update',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const patient = await getPatientById(id);

        if (!patient) {
            return res.status(400).json({
                message: 'Patient not found',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        patient.first_name = first_name;
        patient.last_name = last_name;
        patient.PESEL = PESEL;
        patient.address = address;
        await patient.save();

        return res.status(200).json({
            message: 'Patient updated successfully',
            data: patient,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        });
    }
}

