# API_RESTAURANT

## **EMPLOYEES**
### ![GET](./assets/img/get.png) GET_EMPLOYEES
>/api/employees/

#### Response

```json
    [
        {
            "id": 1,
            "name": "Joseph Climber",
            "login": "joseph",
            "is_admin": False,
            "cpf": "047222222222"
        },
        {
            "id": 2,
            "name": "Irineu Rodrigues",
            "login": "irineu",
            "is_admin": True,
            "cpf": "047333333333"
        }
    ]
```

### ![GET](./assets/img/get.png) GET_EMPLOYEE
>/api/employees/<employee_id: int>/


#### Response
```json
    {
        "id": 1,
        "name": "Joseph Climber",
        "login": "joseph",
        "is_admin": False,
        "cpf": "047222222222"
    }
```

### ![POST](./assets/img/post.png) CREATE_EMPLOYEE
>/api/employees/

#### Body
```json
    {
        "name": "Joseph Climber",
        "login": "joseph",
        "password": "123456",
        "is_admin": False,
        "cpf": "047222222222"
    }
```

#### Response
```json
    {
        "id": 1,
        "name": "Joseph Climber",
        "login": "joseph",
        "is_admin": False,
        "cpf": "047222222222"
    }
```

### ![PATCH](./assets/img/patch.png) UPDATE_EMPLOYEE
>/api/employees/<employee_id: int>/

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
        "is_admin": False,
        "cpf": "047222222222"
    }
```

***

## **USERS**

### ![GET](./assets/img/get.png) GET_USERS
>/api/users/

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

### ![GET](./assets/img/get.png) GET_USER
>/api/users/<user_cpf: str>/

#### Response

```json
    {
        "id": 1,
        "name": "Joseph Climber",
        "cpf": "047222222222",
        "total_spent": 345.22
    }
```

### ![POST](./assets/img/post.png) CREATE_USER
>/api/users/

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

### ![PATCH](./assets/img/patch.png) UPDATE_USER
>/api/users/<user_id: int>/

#### Body
```json
    {
        "id": 1,
        "name": "Joseph Rodrigues",
        "total_spent": 522.35
    }
```

#### Response
```json
    {
        "id": 1,
        "name": "Joseph Climber",
        "cpf": "047222222222",
        "total_spent": 522.35
    }
```



tables -> GET POST PATCH
endpoint(GET_TABLES) = '/api/tables?empty=<empty: bool>/' -> GET
endpoint(GET_TABLE) = '/api/tables/<table_id: int>/' -> GET
endpoint(CREATE_TABLE) = '/api/tables/' -> POST
endpoint(UPDATE_TABLE) = '/api/tables/<table_id: int>/' -> PATCH
endpoint(DELETE_TABLE) = '/api/tables/<table_id: int>/' -> DELETE
endpoint(LOGIN_TABLE) = '/api/tables/login' -> POST


{
    id:
    number:
    user: '/api/user/user_id'
    orders_list: '/api/orders/table_id'
}


orders -> GET POST PATCH
endpoint(GET_ORDERS) = '/api/orders?
                        cooking=<cooking: bool>
                        &ready=<ready: bool>
                        &delivered=<delivered: bool>/' -> GET (OS 3 SAO OPCIONAIS)
endpoint(GET_ORDER_BY_TABLE) = '/api/orders/<table_id: int>?
                                cooking=<cooking: bool>
                                &ready=<ready: bool>
                                &delivered=<delivered: bool>/' -> GET (POR PADRAO RETORNAR PAID = FALSE)
endpoint(UPDATE_ORDER) = '/api/orders/<order_id: int>/' -> PATCH
endpoint(DELETE_ORDER) = '/api/orders/<order_id: int>/' -> DELETE
endpoint(CREATE_ORDER) = '/api/orders/' -> POST


products -> GET POST PATCH
endpoint(GET_PRODUCTS) = '/api/products?
                          section=<section: bool>
                          ?veggie=<veggie: bool>' -> GET
endpoint(GET_PRODUCT) = '/api/products/<product_id: int>/' -> GET
endpoint(CREATE_PRODUCT) = '/api/products/' -> POST
endpoint(UPDATE_PRODUCT) = '/api/products/<product_id: int>/' -> PATCH
endpoint(DELETE_PRODUCT) = '/api/products/<product_id: int>/' -> DELETE