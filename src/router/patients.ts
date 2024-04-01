import { deletePatient, getAllPatients, getPatient, registerPatient, updatePatient } from '../controllers/patients';
import express from 'express';
import { isAuthenticated, isAdmin, isOwner } from '../middlewares';

export default (router: express.Router) => {
    router.get('/patients', isAuthenticated, getAllPatients);
    router.get('/patients/:id', isAuthenticated, getPatient);
    router.post('/patients', isAuthenticated, isAdmin, registerPatient);
    router.delete('/patients/:id', isAuthenticated, isAdmin, deletePatient);
    router.patch('/patients/:id', isAuthenticated, isOwner, updatePatient);
};
