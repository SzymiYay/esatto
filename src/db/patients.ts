import mongoose from "mongoose";

const AddressSchema = new mongoose.Schema({
    city: {
      type: String,
      required: true
    },
    street: {
      type: String,
      required: true
    },
    zipcode: {
      type: String,
      required: true
    }
  });

const PatientSchema = new mongoose.Schema({
    first_name: {
        type: String,
        required: true,
    },
    last_name: {
        type: String,
        required: true,
    },
    PESEL: {
        type: String,
        required: true,
    },
    address: {
        type: AddressSchema,
        required: true,
    }
});

export const PatientModel = mongoose.model('Patient', PatientSchema);

export const getPatients = () => PatientModel.find();
export const getPatientById = (id: string) => PatientModel.findById(id);
export const getPatientByName = (name: string) => PatientModel.findOne({ name });
export const createPatient = (values: Record<string, any>) => new PatientModel(values).save().then((patient) => patient.toObject());
export const deletePatientById = (id: string) => PatientModel.findByIdAndDelete({_id: id});
export const updatePatientById = (id: string, values: Record<string, any>) => PatientModel.findByIdAndUpdate(id, values);
