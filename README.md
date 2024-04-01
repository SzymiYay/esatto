# PATIENT SERVICE
This is a simple application that allows you to manage patients in a hospital. You can add, delete, update and get patients. The application is written in Typescript. The database is MongoDB.

## Built With
- Node
- Typescript
- Express
- MongooseDB


## Getting Started
1. Clone the repo
   ```sh
   git clone https://github.com/SzymiYay/esatto
   ```
2. To start the project, you need to have Node.js installed on your computer. If you don't have it, you can download it from the official website: https://nodejs.org/en/
3. Install NPM packages
   ```sh
   npm install
   ```
4. Make sure you are on branch node-v1
   ```sh
   git checkout node-v1
   ```
5. Create a .env file in the root directory and add the following variables:
   ```sh
    MONGO_URL=your_mongo_url
    ```
    You can get the URL from the MongoDB website: https://www.mongodb.com/cloud/atlas. Create a new cluster and get the URL.
5. Start the project
    ```sh
    npm start
    ```

## Usage
The application is a simple REST API. You can use Postman to test the endpoints. Below are the endpoints that you can use:

### LOGIN, REGISTER
- POST /auth/signup
Body:
```json
{
    "username": "your_username",
    "email": "your_email",
    "password": "your_password"
}
```
- POST /auth/login
Body:
```json
{
    "email": "your_email",
    "password": "your_password"
}
```
- GET /auth/logout

### USERS
- GET /users/:id
- GET /users
```json
{
    "message": "Users fetched successfully",
    "data": [
        {
            "_id": "660ace22f87c3c9097e9d6c4",
            "username": "ja",
            "email": "ja@ja.com",
            "role": "user",
            "patients": [],
            "__v": 0
        },
        {
            "_id": "660ad5d74a017d8774ce87d6",
            "username": "test",
            "email": "test@test.com",
            "role": "admin",
            "patients": [
                {
                    "patientId": "660ada4a623d9c5fbfe3e719",
                    "_id": "660ada4a623d9c5fbfe3e71c"
                }
            ],
            "__v": 0
        }
    ],
    "status": 200,
    "info": "OK"
}
```
- GET /users/:id/patients
```json
{
    "message": "Patients fetched successfully",
    "data": [
        {
            "patientId": {
                "_id": "660ada4a623d9c5fbfe3e719",
                "first_name": "jan",
                "last_name": "kowal",
                "PESEL": "00000000003",
                "address": {
                    "city": "Krakow",
                    "street": "Dluga",
                    "zipcode": "000000",
                    "_id": "660ada4a623d9c5fbfe3e71a"
                },
                "__v": 0
            },
            "_id": "660ada4a623d9c5fbfe3e71c"
        }
    ],
    "status": 200,
    "info": "OK"
}
```
- DELETE /users/:id
- PATCH /users/:id

### PATIENTS
- GET /patients/:id
```json
{
    "message": "Patient fetched successfully",
    "data": {
        "_id": "660ada4a623d9c5fbfe3e719",
        "first_name": "jan",
        "last_name": "kowal",
        "PESEL": "00000000003",
        "address": {
            "city": "Krakow",
            "street": "Dluga",
            "zipcode": "000000",
            "_id": "660ada4a623d9c5fbfe3e71a"
        },
        "__v": 0
    },
    "status": 200,
    "info": "OK"
}
```
- GET /patients
- POST /patients
body:
```json
{
    "first_name": "jan",
    "last_name": "kowal",
    "PESEL": "00000000003",
    "address": {
        "city": "Krakow",
        "street": "Dluga",
        "zipcode": "000000"
    }
}
```
body response:
```json
{
    "message": "Patient registered successfully",
    "data": {
        "first_name": "jan",
        "last_name": "kowal",
        "PESEL": "00000000003",
        "address": {
            "city": "Krakow",
            "street": "Dluga",
            "zipcode": "000000",
            "_id": "660ada4a623d9c5fbfe3e71a"
        },
        "_id": "660ada4a623d9c5fbfe3e719",
        "__v": 0
    },
    "status": 200,
    "info": "OK"
}
```
- DELETE /patients/:id
- PATCH /patients/:id


## Contributing
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/new-feature`)
3. Commit your Changes (`git commit -m 'Add some new-feature'`)
4. Push to the Branch (`git push origin feature/new-feature`)
5. Open a Pull Request


## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact
Szymon Frączek - szymoon09@gmail.com
