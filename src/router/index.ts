import express from 'express';

import authentication from './authentication';
import users from './users';
import patients from './patients';

const router = express.Router();

export default (): express.Router => {
    authentication(router);
    users(router);
    patients(router);
    
    return router;
}
