from flask import jsonify, request
from .helpers import add_commit, delete_commit
from app.models.restaurant_table_model import RestaurantTableModel
from http import HTTPStatus


def create_table(data: dict):
    new_table = RestaurantTableModel(**data)

    add_commit(new_table)

    return jsonify(new_table)


def login_table():
    ...


def delete_table(table_id: int):
    found_table = RestaurantTableModel.query.get(table_id)

    if not found_table:
        return {"status": "table not found"}, HTTPStatus.NOT_FOUND

    delete_commit(found_table)

    return "", HTTPStatus.NO_CONTENT


def update_table(data: dict, table_id: int):

    found_table = RestaurantTableModel.query.get(table_id)

    if not found_table:
        return {"status": "table not found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(found_table, key, value)

    add_commit(found_table)

    return jsonify(found_table)


def get_table(table_id: int):
    found_table_id = RestaurantTableModel.query.filter(
        RestaurantTableModel.id == table_id
    ).all()

    return found_table_id


# tables -> GET POST PATCH
# endpoint(GET_TABLES) = '/api/tables?empty=<empty: bool>/' -> GET

# endpoint(GET_TABLE) = '/api/tables/<table_id: int>/' -> GET


# endpoint(LOGIN_TABLE) = '/api/tables/login' -> POST
