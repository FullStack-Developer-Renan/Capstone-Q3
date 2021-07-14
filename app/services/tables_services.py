from flask import request
from .helpers import add_commit, delete_commit
from flask_restful import reqparse
from app.models.restaurant_table_model import RestaurantTableModel
from http import HTTPStatus
from flask_jwt_extended import create_access_token

def get_all() -> list:
    table = RestaurantTableModel.query.all()

    response = []

    for value in table:
        response.append(
            {
                "id": value.id,
                "seats": value.seats,
                "number": value.number,
                "total": value.total,
                "empty": value.empty,
            }
        )

    return response, HTTPStatus.OK


# endpoint(CREATE_TABLE) = '/api/tables/' -> POST
def create_table() -> RestaurantTableModel:
    parser = reqparse.RequestParser()

    parser.add_argument("number", type=int, required=True)
    parser.add_argument("login", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    new_table: RestaurantTableModel = RestaurantTableModel(**parser.parse_args())

    add_commit(new_table)

    return {
        "id": new_table.id,
        "number": new_table.number,
        "login": new_table.login,
    }


# endpoint(LOGIN_TABLE) = '/api/tables/login' -> POST
def login_table():

    parser = reqparse.RequestParser()

    parser.add_argument("login", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    data = parser.parse_args()

    user: RestaurantTableModel = RestaurantTableModel.query.filter_by(
        login=data["login"]
    ).first()

    if not user:
        return {
            "message": "User not Found"
        }, HTTPStatus.NOT_FOUND

    if user.check_password(data['password']):
        token = create_access_token(identity=user)
        return {
            "token": token
        }, HTTPStatus.OK
    else:
        return {
            "message": "Invalid password or login information"
        }, HTTPStatus.UNAUTHORIZED


# endpoint(DELETE_TABLE) = '/api/tables/<table_id: int>/' -> DELETE
def delete_table(table_id) -> str:
    found_table = RestaurantTableModel.query.get(table_id)

    if not found_table:
        return {"status": "table not found"}, HTTPStatus.NOT_FOUND

    delete_commit(found_table)

    return "", HTTPStatus.NO_CONTENT


# endpoint(UPDATE_TABLE) = '/api/tables/<table_id: int>/' -> PATCH
def update_table(table_id: int) -> RestaurantTableModel:
    parser = reqparse.RequestParser()

    parser.add_argument("seats", type=int, required=False)
    parser.add_argument("number", type=int, required=False)
    parser.add_argument("total", type=int, required=False)
    parser.add_argument("empty", type=bool, required=False)
    parser.add_argument("password", type=str, required=False)
    parser.add_argument("login", type=str, required=False)

    data = parser.parse_args(strict=True)

    table = RestaurantTableModel.query.get(table_id)

    if not table:
        return {"status": "table not found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        if value != None:
            setattr(table, key, value)

    add_commit(table)

    return {
        "id": table.id,
        "seats": table.seats,
        "number": table.number,
        "total": table.total,
        "empty": table.empty,
        "login": table.login,
    }, HTTPStatus.OK


# endpoint(GET_TABLE) = '/api/tables/<table_id: int>/' -> GET
def get_by_id(table_id) -> RestaurantTableModel:
    table = RestaurantTableModel.query.get(table_id)

    if table:
        return {
            "id": table.id,
            "seats": table.seats,
            "number": table.number,
            "total": table.total,
            "empty": table.empty,
        }, HTTPStatus.OK

    return {"status": "table not found!"}, HTTPStatus.NOT_FOUND


# endpoint(GET_TABLES) = '/api/tables?empty=<empty: bool>/' -> GET
def get_tables() -> dict:
    args = request.args
    response = []

    if "empty" in args:
        empty = args["empty"]
        query = RestaurantTableModel.query.filter_by(empty=empty).all()
        response += query

        list = []
        for table in response:
            list.append(
                {
                    "id": table.id,
                    "seats": table.seats,
                    "number": table.number,
                    "total": table.total,
                    "empty": table.empty,
                }
            )

        return list

    return get_all()
