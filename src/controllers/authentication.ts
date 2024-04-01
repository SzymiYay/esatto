import express from 'express';
import { getReasonPhrase } from 'http-status-codes';

import { createUser, getUserByEmail, getUserBySessionToken } from '../db/users';
import { random, authentication } from '../helpers';

export const login = async (req: express.Request, res: express.Response) => {
    try {
        const {email, password} = req.body;

        if (!email || !password) {
            return res.status(400).json({
                message: 'Missing required fields - email or password',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const user = await getUserByEmail(email).select('+authentication.salt +authentication.password');

        if (!user) {
            return res.status(400).json({
                message: 'User not found',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const expectedHash = authentication(user.authentication.salt, password);

        if (expectedHash !== user.authentication.password) {
            return res.status(403).json({
                message: 'Invalid password',
                status: 403,
                info: getReasonPhrase(403),
            });
        }

        const salt = random();
        user.authentication.sessionToken = authentication(salt, user._id.toString())

        await user.save();

        res.cookie('token', user.authentication.sessionToken, {
            domain: 'localhost',
            path: '/',
            httpOnly: false,
        })

        return res.status(200).json({
            message: 'User logged in successfully',
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
        });
    }
}

export const register = async (req: express.Request, res: express.Response) => {
    try {
        const { username, email, password } = req.body;

        if (!username || !email || !password) {
            return res.status(400).json({
                message: 'Missing required fields - username, email or password',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const existingUser = await getUserByEmail(email);
        
        if (existingUser) {
            return res.status(400).json({
                message: 'User already exists',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const salt = random();
        const user = await createUser({
            username,
            email,
            authentication: {
                salt,
                password: authentication(salt, password),
            },
        });

        return res.status(200).json({
            message: 'User registered successfully',
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
        });
    }
}

export const logout = async (req: express.Request, res: express.Response) => {
    try {
        const sessionToken = req.cookies['token'];

        if (!sessionToken) {
            return res.status(400).json({
                message: 'Token not found',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        const user = await getUserBySessionToken(sessionToken);

        if (!user) {
            return res.status(400).json({
                message: 'User not found',
                status: 400,
                info: getReasonPhrase(400),
            });
        }

        user.authentication.sessionToken = null;

        await user.save();

        return res.status(200).send({
            message: 'User logged out successfully',
            status: 200,
            info: getReasonPhrase(200)
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