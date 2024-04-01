import mongoose from "mongoose";

const UserSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
    },
    email: {
        type: String,
        required: true,
    },
    authentication: {
        password: {
            type: String,
            required: true,
            select: false,
        },
        salt: {
            type: String,
            required: true,
            select: false,
        },
        sessionToken: {
            type: String,
            select: false,
        },
    },
    role: {
        type: String,
        enum: ['admin', 'user'],
        default: 'user',
        required: true,
    },
    patients: [{
        patientId: {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'Patient',
        },
    }],
});

export const UserModel = mongoose.model('User', UserSchema);

export const getUsers = () => UserModel.find();
export const getUserByEmail = (email: string) => UserModel.findOne({ email });
export const getUserBySessionToken = (sessionToken: string) => UserModel.findOne({ 'authentication.sessionToken': sessionToken }); 
export const getUserById = (id: string) => UserModel.findById(id);
export const getPatientsByUserId = (id: string) => UserModel.findById(id).populate('patients.patientId');
export const createUser = (values: Record<string, any>) => new UserModel(values).save().then((user) => user.toObject());
export const deleteUserById = (id: string) => UserModel.findByIdAndDelete({_id: id});
export const updateUserById = (id: string, values: Record<string, any>) => UserModel.findByIdAndUpdate(id, values);
export const updatePatients = (
    id: string,
    patient: {
        patientId: string,
    }) => UserModel.findByIdAndUpdate(id, { $push: { patients: patient } }, { new: true });
