# **FLASK_DATABASE_REST - API**

This app exposes endPoints which can be used to perform various DataBase operations (e.g. Fetch, Insert, Update and Delete ) on the database stored on server.

## Usage

### Users endpoint
GET http://127.0.0.1:5000/product

RESPONSE
```json

[
  {
    "id": 1,
    "name": "Rcsdd",
    "description": "A short 200 words description is enough, why to live like a slave of
  yourself, live free, you can, you just have to be brave enough to accept the truth, the fact that nothing else is
  stoping you other than yourself.",
    "price": 99,
    "qty": 3
  },
  {
    "id": 2,
    "name": "RC Helipcopter",
    "description": "a short description",
    "price": 250,
    "qty": 10
  }
]
```

GET http://127.0.0.1:5000/product/2
```json
{
  "id": 2,
  "name": "RC Helipcopter",
  "description": "a short description",
  "price": 250,
  "qty": 10
}
```

<hr>

* Insert
  
POST http://127.0.0.1:5000/product

REQUEST
```json
{
  "name": "RC Helipcopter",
  "description": "a short description",
  "price": 250,
  "qty": 10
}
```
RESPONSE
```json
{
  "id": 2,
  "name": "RC Helipcopter",
  "description": "a short description",
  "price": 250,
  "qty": 10
}
```

<hr>

* Update
  
PUT http://127.0.0.1:5000/product/1

REQUEST
```json
{
  "name": "RC Coper",
  "description": "a description",
  "price": 250,
  "qty": 10
}
```
RESPONSE
```json
{
  "id": 2,
  "name": "RC Helipcopter",
  "description": "a short description",
  "price": 250,
  "qty": 10
}
```
DELETE http://127.0.0.1:5000/product/1

RESPONSE
```json
{
  "id": 2,
  "name": "RC Helipcopter",
  "description": "a short description",
  "price": 250,
  "qty": 10
}
```

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://rohitkrtiwari.github.io/Portfolio)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rohitkrtiwari/)
