import express from 'express';

import { deleteUser, getAllUsers, getPatientsByUserId_, getUserById_, updatePatients, updateUser } from '../controllers/users';
import { isAuthenticated, isAdminOrOwner, isAdmin, isOwner } from '../middlewares';

export default (router: express.Router) => {
    router.get('/users', isAuthenticated, isAdmin, getAllUsers);
    router.get('/users/:id', isAuthenticated, isAdminOrOwner, getUserById_)
    router.get('/users/:id/patients', isAuthenticated, isOwner, getPatientsByUserId_);
    router.delete('/users/:id', isAuthenticated, isAdminOrOwner, deleteUser);
    router.patch('/users/:id', isAuthenticated, isAdminOrOwner, updateUser);
    router.patch('/users/:id/add', isAuthenticated, isAdminOrOwner, updatePatients);
};