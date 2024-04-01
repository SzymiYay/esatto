def get_description():
    return  """
This is a simple API for patients in hospital. It allows you to create users, patients.

## How to login
1. Create a user (see [Create a user](#create-a-user))
2. Login with the created user (see [Get a token](#get-a-token)), you will get an access token and a refresh token.
3. When the access token expires:
    1. Get a new access token with the refresh token (see [Refresh a token](#refresh-a-token))
    2. Login again (see [Get a token](#get-a-token))


## API documentation
1. [Base URL](#base-url)
2. [Authentication](#authentication)
    1. [Get a token](#get-a-token)
    2. [Refresh a token](#refresh-a-token)
3. [Users](#users)
    1. [Create a user](#create-a-user)
    2. [Get user details](#get-user-details)
    3. [Get user patients](#get-user-patients)
    4. [Create a patient](#create-a-patient)
    5. [Delete a patient](#delete-a-patient)


## Base URL
/api/v1

## Authentication

### Get a token

This API uses OAuth2 with password flow. You can get a token by sending a POST request to `/auth/login` with the following body: 

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

The response will be a JSON object with the following structure:

```json
{
    "access_token": "your_access_token",
    "refresh_token": "your_refresh_token",
    "token_type": "bearer"
}
```

### Refresh a token

You can use the access token to access the API. The refresh token can be used to get a new access token when the current one expires. To do so, send a POST request to `/auth/token/refresh` with the following body:

```json
{
    "username": "your_username",
    "password": "your_password",
}
```

The response will be a JSON object with the following structure:

```json
{
    "refresh_token": "your_refresh_token",
}
```

## Users

### Create a user

To create a user, send a POST request to `/auth/signup` with the following body:

```json
{
    "username": "your_username",
    "email": "your_email",
    "password": "your_password"
}
```

### Get user details

To get the details of the current user, send a GET request to `/users/profile`. The response will be a JSON object with the following structure:

```json
{
    "username": "your_username",
    "email": "your_email"
}
```

### Get user patients

To get the patients of the current user, send a GET request to `/users/patients`. The response will be a JSON object with the following structure:

```json
[
  {
    "first_name": "name",
    "last_name": "name",
    "PESEL": "PESEL",
    "city": "city",
    "street": "street",
    "zip_code": "zip_code",
    "id": 3,
    "user_id": 1
  }
]
```

### Create a patient

To create a patient, send a POST request to `/users/patients` with the following body:

```json
{
  "first_name": "name",
  "last_name": "name",
  "PESEL": "PESEL",
  "city": "city",
  "street": "street",
  "zip_code": "zip_code"
}
```

### Delete a patient

To delete a patient, send a DELETE request to `/users/patients/{patient_id}` with the following body:

```json
{
    "patient_id": 1
}
```

"""