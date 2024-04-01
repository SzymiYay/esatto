import express from 'express';
import { getReasonPhrase } from 'http-status-codes';

import { deleteUserById, getPatientsByUserId, getUserById, getUsers } from '../db/users';

export const getAllUsers = async (req: express.Request, res: express.Response) => {
    try {
        const users = await getUsers();

        return res.status(200).json({
            message: 'Users fetched successfully',
            data: users,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}

export const getUserById_ = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;

        const user = await getUserById(id);

        return res.status(200).json({
            message: 'User fetched successfully',
            data: user,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}

export const getPatientsByUserId_ = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;

        const user = await getPatientsByUserId(id);

        return res.status(200).json({
            message: 'Patients fetched successfully',
            data: user.patients,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}

export const deleteUser = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;

        const deletedUser = await deleteUserById(id);

        return res.json({
            message: 'User deleted successfully',
            data: deletedUser,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}

export const updateUser = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;
        const { username } = req.body;

        if (!username) {
            return res.status(400).json({
                message: 'Missing required fields - username',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const user = await getUserById(id);

        user.username = username;
        await user.save();

        return res.status(200).json({
            message: 'User updated successfully',
            data: user,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}

export const updatePatients = async (req: express.Request, res: express.Response) => {
    try {
        const { id } = req.params;
        const { patients } = req.body;

        if (!patients) {
            return res.status(400).json({
                message: 'Missing required fields - patients',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const user = await getUserById(id);

        patients.forEach((patient: any) => {
            user.patients.push(patient);
        });

        await user.save();

        return res.status(200).json({
            message: 'Patients updated successfully',
            data: user,
            status: 200,
            info: getReasonPhrase(200),
        }).end();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}