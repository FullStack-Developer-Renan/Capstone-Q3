from flask import jsonify, current_app
from .helpers import add_commit
from flask_restful import reqparse
from app.models.restaurant_table_model import RestaurantTableModel
from http import HTTPStatus


def get_by_id(table_id) -> RestaurantTableModel:
    table = RestaurantTableModel.query.get(table_id)
    if table:
        return table, HTTPStatus.OK
    return {}, HTTPStatus.NOT_FOUND


def get_all() -> list[RestaurantTableModel]:
    table_list: list[RestaurantTableModel] = RestaurantTableModel.query.all()
    return jsonify(table_list), HTTPStatus.OK


# endpoint(CREATE_TABLE) = '/api/tables/' -> POST
def create_table() -> RestaurantTableModel:
    parser = reqparse.RequestParser()

    parser.add_argument("seats", type=int, required=True)
    parser.add_argument("number", type=int, required=True)
    parser.add_argument("total", type=int, required=True)
    parser.add_argument("empty", type=bool, required=True)
    parser.add_argument("password", type=str, required=True)

    password = parser.pop("password")
    new_table: RestaurantTableModel = RestaurantTableModel(
        **parser.parse_args(strict=True)
    )
    new_table.password = password

    add_commit(new_table)

    return new_table


def login_table():
    ...


# endpoint(DELETE_TABLE) = '/api/tables/<table_id: int>/' -> DELETE
def delete_table(table_id: int):
    session = current_app.db.session

    found_table = RestaurantTableModel.query.get(table_id)

    if not found_table:
        return {"status": "table not found"}, HTTPStatus.NOT_FOUND

    session.delete(found_table)

    return "", HTTPStatus.NO_CONTENT


# endpoint(UPDATE_TABLE) = '/api/tables/<table_id: int>/' -> PATCH
def update_table(table_id: int) -> RestaurantTableModel:
    parser = reqparse.RequestParser()

    parser.add_argument("seats", type=int, required=False)
    parser.add_argument("number", type=int, required=False)
    parser.add_argument("total", type=int, required=False)
    parser.add_argument("empty", type=bool, required=False)
    parser.add_argument("password", type=str, required=False)

    table = get_by_id(table_id)

    if not table:
        return {"status": "table not found"}, HTTPStatus.NOT_FOUND

    for key, value in parser.parse_args(strict=True):
        setattr(table, key, value)

    add_commit(table)

    return table, HTTPStatus.OK


# endpoint(GET_TABLE) = '/api/tables/<table_id: int>/' -> GET
def get_table(table_id: int):
    parser = reqparse.RequestParser()

    parser.add_argument("seats", type=int, required=True)
    parser.add_argument("number", type=int, required=True)
    parser.add_argument("total", type=int, required=True)
    parser.add_argument("empty", type=bool, required=True)
    parser.add_argument("password", type=str, required=True)

    table = get_by_id(table_id)

    add_commit(parser)

    return table, HTTPStatus.OK


# tables -> GET POST PATCH

# endpoint(GET_TABLES) = '/api/tables?empty=<empty: bool>/' -> GET
# endpoint(LOGIN_TABLE) = '/api/tables/login' -> POST
