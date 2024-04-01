# PATIENT SERVICE

- [Prerequisites](#prerequisites)
    - [Tools](#tools)
    - [Languages](#languages)
- [Basics of the project](#basics-of-the-project)
  - [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Prerequisites
Scripts are written for all platforms, but they were tested only on MacOS.

### Tools
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)

## Basics of the project
### Architecture
Project consists of 1 microservice:
- **FastAPI** service that provides REST API that allows us to get data about measurements from the connected devices.

```json
// GET
// /api/v1/users/patients
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

## Getting Started
1. Clone the repo
```sh
git clone https://github.com/SzymiYay/esatto
```
2. Set branch
```sh
git checkout python-v2
```
3. Run the project
```sh
docker-compose up
```
4. Open the browser and go to the following address:
```sh
http://localhost:8000/docs
```


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
