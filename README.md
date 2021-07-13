# API_RESTAURANT

## **EMPLOYEES**

### ![GET](./assets/img/GET.svg) GET_EMPLOYEES


```
/api/employees/
```
#### Header
```
```
#### Response

```json
[
    {
        "id": 1,
        "name": "Joseph Climber",
        "login": "joseph",
        "is_admin": "False",
        "cpf": "047222222222"
    },
    {
        "id": 2,
        "name": "Irineu Rodrigues",
        "login": "irineu",
        "is_admin": "True",
        "cpf": "047333333333"
    }
]
```
<br>
<br>

### ![GET](./assets/img/GET.svg) GET_EMPLOYEE
```
/api/employees/<employee_id: int>/
```
#### Header
```
```
#### Response
```json
{
    "id": 1,
    "name": "Joseph Climber",
    "login": "joseph",
    "is_admin": "False",
    "cpf": "047222222222"
}
```
<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_EMPLOYEE
```
/api/employees/
```
#### Body
```json
{
    "name": "Joseph Climber",
    "login": "joseph",
    "password": "123456",
    "is_admin": "False",
    "cpf": "047222222222"
}
```

#### Response
```json
{
    "id": 1,
    "name": "Joseph Climber",
    "login": "joseph",
    "is_admin": "False",
    "cpf": "047222222222"
}
```
<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_EMPLOYEE
```
/api/employees/<employee_id: int>/
```
#### Header
```
```
#### Body
```json
{
    "name": "Joseph Rodrigues",
}
```

#### Response
```json
{
    "id": 1,
    "name": "Joseph Rodrigues",
    "login": "joseph",
    "is_admin": "False",
    "cpf": "047222222222"
}
```
<br>
<br>

***

### ![DELETE](./assets/img/DELETE.svg) DELETE_EMPLOYEE
```
/api/employees/<employee_id: int>/
```
#### Header
```
```

#### Response
```json
""
```
<br>
<br>

***

## **USERS**
<br>


### ![GET](./assets/img/GET.svg) GET_USERS
```
/api/users/
```
#### Header
```
```
#### Response

```json
[
    {
        "id": 1,
        "name": "Joseph Climber",
        "cpf": "047222222222",
        "total_spent": 345.22
    },
    {
        "id": 2,
        "name": "Irineu Cleber",
        "cpf": "047333333333",
        "total_spent": 57.48
    },
]
```
<br>
<br>

### ![GET](./assets/img/GET.svg) GET_USER
```
/api/users/<user_cpf: str>/
```
#### Header
```
```
#### Response

```json
{
    "id": 1,
    "name": "Joseph Climber",
    "cpf": "047222222222",
    "total_spent": 345.22
}
```
<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_USER
```
/api/users/
```
#### Header
```
```
#### Body
```json
{
    "name": "Joseph Climber",
    "cpf": "047222222222"
}
```

#### Response
```json
{
    "id": 1,
    "name": "Joseph Climber",
    "cpf": "047222222222",
    "total_spent": 0
}
```
<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_USER
```
/api/users/<user_id: int>/
```
#### Header
```
```
#### Body
```json
{
    "name": "Joseph Rodrigues",
    "total_spent": 522.35
}
```

#### Response
```json
{
    "id": 1,
    "name": "Joseph Rodrigues",
    "cpf": "047222222222",
    "total_spent": 522.35
}
```
<br>
<br>

***
## **TABLES**
<br>

### ![GET](./assets/img/GET.svg) GET_TABLES
```
/api/tables?empty=<empty: bool>/
```
#### Header
```
```
#### Response
```json
[
    {
        "id": 1,
        "number": 1,
        "seats": 6,
        "user": {
                    "id": 1,
                    "name": "Joseph Climber",
                    "cpf": "047222222222",
                    "total_spent": 522.35
                },
        "total": 127.48,
        "empty": "False",
        "orders_list": "/api/orders/1"
    },
    {
        "id": 2,
        "number": 1,
        "seats": 6,
        "user": {},
        "total": 127.48,
        "empty": "True",
        "orders_list": "/api/orders/2"
    }
]
```
<br>
<br>

### ![GET](./assets/img/GET.svg) GET_TABLE
```
/api/tables/table_id=<table_id: int>/
```
#### Header
```
```
#### Response
```json
{
    "id": 1,
    "number": 1,
    "seats": 6,
    "user": {
                "id": 1,
                "name": "Joseph Climber",
                "cpf": "047222222222",
                "total_spent": 522.35
            },
    "total": 127.48,
    "empty": "False",
    "orders_list": "/api/orders/1"
}
```
<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_TABLE
```
/api/tables/
```
#### Header
```
```
#### Body
```json
{
    "login": "table01",
    "password": "table01",
    "number": 1,
    "seats": 6
}
```
#### Response
```json
{
    "id": 1,
    "login": "table01",
    "number": 1,
    "seats": 6,
    "empty": "True",
}
```
<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_TABLE
```
/api/tables/<table_id: int>/
```
#### Header
```
```
#### Body
```json
{
    "number": 2,
    "seats": 4
}
```
#### Response
```json
{
    "id": 1,
    "number": 2,
    "seats": 4,
    "user": {
                "id": 1,
                "name": "Joseph Climber",
                "cpf": "047222222222",
                "total_spent": 522.35
            },
    "total": 127.48,
    "empty": "False",
    "orders_list": "/api/orders/1"
}
```
<br>
<br>

### ![DELETE](./assets/img/DELETE.svg) DELETE_TABLE
```
/api/tables/<table_id: int>/
```
#### Header
```
```
#### Response
```js
    ''
```
<br>
<br>

### ![POST](./assets/img/POST.svg) LOGIN_TABLE
```
/api/tables/login
```
#### Header
```
```
#### Body
```json
{
    "login": "Irineu",
    "password": "12345"
}
```
#### Response
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjIxNDA3NSwianRpIjoiMWJjMDE5ZTktNzY2OS00MzJmLWJhMDctMzE0MjgxZTg0ODU5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MiwibmFtZSI6Ikx1Y2FzIEpvc2Vmb3ZpY3oiLCJsb2dpbiI6Imx1Y2FzIn0sIm5iZiI6MTYyNjIxNDA3NSwiZXhwIjoxNjI2MjE0OTc1fQ.Mj5yzf4ENLntgmnTs8Hvlvwqa_FI_T1fh_1uQiKy6fU"
}
```
<br>
<br>

***
## **ORDERS**
<br>

### ![GET](./assets/img/GET.svg) GET_ORDERS
```
/api/orders?cooking=<cooking: bool>&ready=<ready: bool>&delivered=<delivered: bool>
```
#### Header
```
```
#### Response
```json
[
    {
        "id": 1,
        "date": ,//decidir formato da data
        "table_number": 5,
        "cooking": "False",
        "ready": "False",
        "delivered": "False",
        "paid": "False",
        "products": [
                        {
                            "id": 1,
                            "name": "Risoto Carbonara",
                            "quantity": 2,
                            "price": 7.80
                        },
                        {
                            "id": 3,
                            "name": "Fettuccine com molho Marzano",
                            "quantity": 1,
                            "price": 15.00
                        }
                    ],
        "total_products": 30.60
    },
    {
        "id": 2,
        "date": ,//decidir formato da data
        "table_number": 3,
        "cooking": "True",
        "ready": "False",
        "delivered": "False",
        "paid": "False",
        "products": [
                        {
                            "id": 4,
                            "name": "Raviolli de Ricota",
                            "quantity": 1,
                            "price": 10.00
                        }
                    ],
        "total_products": 10.00
    }
]
```
<br>
<br>

### ![GET](./assets/img/GET.svg) GET_ORDERS_BY_TABLE
```
/api/orders/table/<table_id: int>?cooking=<cooking: bool>&ready=<ready: bool>&delivered=<delivered: bool>/
```
#### Header
```
```
#### Response
```json
[
    {
        "id": 1,
        "date": ,//decidir formato da data
        "table_number": 5,
        "cooking": "False",
        "ready": "False",
        "delivered": "False",
        "products": [
                        {
                            "id": 1,
                            "name": "Risoto Carbonara",
                            "quantity": 2,
                            "price": 7.80
                        },
                        {
                            "id": 3,
                            "name": "Fettuccine com molho Marzano",
                            "quantity": 1,
                            "price": 15.00
                        }
                    ],
        "total_products": 30.60
    }
]
```
<br>
<br>

### ![POST](./assets/img/POST.svg) CREATE_ORDER
```
/api/orders/
```
#### Header
```
```
#### Body
```json
{
    "date": ,//decidir formato da data
    "table_id": 5,
    "products": [
                    {
                        "id": 1,
                        "name": "Risoto Carbonara",
                        "quantity": 2
                    },
                    {
                        "id": 3,
                        "name": "Fettuccine com molho Marzano",
                        "quantity": 1
                    }
                ]
}
```

#### Response
```json
{
    "id": 1,
    "date": ,//decidir formato da data
    "table_number": 5,
    "cooking": "False",
    "ready": "False",
    "delivered": "False",
    "products": [
                    {
                        "id": 1,
                        "name": "Risoto Carbonara",
                        "quantity": 2,
                        "price": 7.80
                    },
                    {
                        "id": 3,
                        "name": "Fettuccine com molho Marzano",
                        "quantity": 1,
                        "price": 15.00
                    }
                ],
    "total_products": 30.60
}

```
<br>
<br>


### ![PATCH](./assets/img/PATCH.svg) UPDATE_ORDER
```
/api/orders/<order_id: int>/
```
#### Header
```
```
#### Body
```json
{
    "cooking": "False",
    "ready": "True",
    "delivered": "False"
}

```
#### Response
```json
[
    {
        "id": 1,
        "date": ,//decidir formato da data
        "table_number": 5,
        "cooking": "False",
        "ready": "True",
        "delivered": "False",
        "products": [
                        {
                            "id": 1,
                            "name": "Risoto Carbonara",
                            "quantity": 2,
                            "price": 7.80
                        },
                        {
                            "id": 3,
                            "name": "Fettuccine com molho Marzano",
                            "quantity": 1,
                            "price": 15.00
                        }
                    ],
        "total_products": 30.60
    }
]
```
<br>
<br>

### ![DELETE](./assets/img/DELETE.svg) DELETE_ORDER
```
/api/orders/<order_id: int>/
```
#### Header
```
```
#### Response
```js
""
```
<br>
<br>

***
## **PRODUCTS**
<br>

### ![GET](./assets/img/GET.svg) GET_PRODUCTS
```
/api/products?section=<section: bool>?veggie=<veggie: bool>
```
#### Header
```
```

#### Response
```json
[
    {
        "id": 1,
        "name": "Risoto Carbonara",
        "section": "Pratos principais",
        "price": 7.80,
        "calories": 587.87
    },
    {
        "id": 3,
        "name": "Fettuccine com molho Marzano",
        "section": "Pratos principais",
        "price": 15.00,
        "calories": 635.22
    }
]

```
<br>
<br>

### ![GET](./assets/img/GET.svg) GET_PRODUCT
```
/api/products/<product_id: int>/
```
#### Header
```
```

#### Response
```json
{
    "id": 1,
    "name": "Risoto Carbonara",
    "section": "Pratos principais",
    "price": 7.80,
    "calories": 587.87 
}
```
<br>
<br>


### ![POST](./assets/img/POST.svg) CREATE_PRODUCT
```
/api/products/
```
#### Header
```
```
#### Body
```json
{
    "name": "Risoto Carbonara",
    "price": 7.80,
    "calories": 587.87 
}
```
#### Response
```json
{
    "id": 1,
    "name": "Risoto Carbonara",
    "section": "None",
    "price": 7.80,
    "calories": 587.87 
}
```
<br>
<br>

### ![PATCH](./assets/img/PATCH.svg) UPDATE_PRODUCT
```
/api/products/<product_id: int>/
```
#### Header
```
```
#### Body
```json
{
    "price": 18.80,
}
```
#### Response
```json
{
    "id": 1,
    "name": "Risoto Carbonara",
    "section": "None",
    "price": 18.80,
    "calories": 587.87 
}
```
<br>
<br>


### ![DELETE](./assets/img/DELETE.svg) UPDATE_PRODUCT
```
/api/products/<product_id: int>/
```
#### Header
```
```
#### Response
```js
""
```
<br>
<br>