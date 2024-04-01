import express from 'express';
import { get, merge } from 'lodash';

import { getUserById, getUserBySessionToken } from '../db/users';
import { getReasonPhrase } from 'http-status-codes';

export const isAuthenticated = async (req: express.Request, res: express.Response, next: express.NextFunction) => {
    try {

        const sessionToken = req.cookies['token'];

        if (!sessionToken) {
            return res.status(403).json({
                message: 'Token not found',
                status: 403,
                info: getReasonPhrase(403),
            });
        }

        const existingUser = await getUserBySessionToken(sessionToken);

        if (!existingUser) {
            return res.status(403).json({
                message: 'User not found',
                status: 403,
                info: getReasonPhrase(403),
            });
        }

        merge(req, {identity: existingUser})

        return next();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}

export const isOwner = (req: express.Request, res: express.Response, next: express.NextFunction) => {
    try {
        
        const { id } = req.params;
        const currentUserId = get(req, 'identity._id') as string;

        if (!currentUserId) {
            return res.status(400).json({
                message: 'User not found',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        // const currentUser = getUserById(currentUserId);

        // if (!currentUser) {
        //     return res.status(400).json({
        //         message: 'User not found',
        //         status: 400,
        //         info: getReasonPhrase(400),
        //     });
        // }

        // if (currentUserId.toString() !== id) {
        //     return res.status(403).json({
        //         message: 'You are not authorized to perform this action',
        //         status: 403,
        //         info: getReasonPhrase(403),
        //     });
        // }

        return next();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}

export const isAdmin = async (req: express.Request, res: express.Response, next: express.NextFunction) => {
    try {
        const currentUserId = get(req, 'identity._id') as string;

        if (!currentUserId) {
            return res.status(400).json({
                message: 'User not found',
                status: 400,
                info: getReasonPhrase(400),
            })
        }

        const currentUser = await getUserById(currentUserId);

        if (!currentUser) {
            return res.status(400).json({
                message: 'User not found',
                status: 400,
                info: getReasonPhrase(400),
            })
        }

        if (currentUser.role !== 'admin') {
            return res.status(403).json({
                message: 'You are not authorized to perform this action',
                status: 403,
                info: getReasonPhrase(403),
            });
        }

        return next();

    } catch (error) {
        console.log(error);
        return res.status(400).json({
            message: error.message,
            status: 400,
            info: getReasonPhrase(400),
        })
    }
}

export const isAdminOrOwner = (req: express.Request, res: express.Response, next: express.NextFunction) => {
    const { id } = req.params;
    const currentUserId = get(req, 'identity._id') as string;
    const currentUserRole = get(req, 'identity.role') as string;

    if (!currentUserId) {
        return res.status(400).json({
            message: 'User not found',
            status: 400,
            info: getReasonPhrase(400),
        });
    }

    if (currentUserRole === 'admin' || currentUserId.toString() === id) {
        next();
    } else {
        return res.status(403).json({
            message: 'You are not authorized to perform this action',
            status: 403,
            info: getReasonPhrase(403),
        });
    }
}
