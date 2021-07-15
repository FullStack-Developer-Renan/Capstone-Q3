from flask import request
from werkzeug.exceptions import NotFound
from .helpers import add_commit, delete_commit
from flask_restful import reqparse
from app.models.restaurant_table_model import RestaurantTableModel
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from app.exc import DuplicatedKeys


def get_all() -> list:
    table = RestaurantTableModel.query.all()

    response = []

    for value in table:
        value_serialize = value.serialize()
        value_serialize["orders_list"] = f"/api/orders?table_id={value.id}"
        response.append(value_serialize)

    return response, HTTPStatus.OK


def get_table_by_login(data) -> RestaurantTableModel:
    table: RestaurantTableModel = RestaurantTableModel.query.filter_by(
        login=data["login"]
    ).first()
    return table


# endpoint(CREATE_TABLE) = '/api/tables/' -> POST
def create_table() -> RestaurantTableModel:

    parser = reqparse.RequestParser()

    parser.add_argument("number", type=int, required=True)
    parser.add_argument("login", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    data = parser.parse_args(strict=True)

    if get_table_by_login(data):
        raise DuplicatedKeys

    new_table: RestaurantTableModel = RestaurantTableModel(**data)

    add_commit(new_table)

    return {
        "id": new_table.id,
        "number": new_table.number,
        "login": new_table.login,
    }


def login_table():

    parser = reqparse.RequestParser()

    parser.add_argument("login", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    data = parser.parse_args(strict=True)

    user: RestaurantTableModel = RestaurantTableModel.query.filter_by(
        login=data["login"]
    ).first()

    if not user:
        raise NotFound

    if user.check_password(data["password"]):
        token = create_access_token(identity=user)
        return {"token": token}, HTTPStatus.OK
    else:
        return {
            "message": "Invalid password or login information"
        }, HTTPStatus.UNAUTHORIZED


def delete_table(table_id) -> str:
    found_table = RestaurantTableModel.query.get(table_id)

    if not found_table:
        raise NotFound

    delete_commit(found_table)

    return "", HTTPStatus.NO_CONTENT


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
        raise ("Error")

    for key, value in data.items():
        if value != None:
            setattr(table, key, value)

    add_commit(table)

    return table.serialize(), HTTPStatus.OK


def get_by_id(table_id) -> RestaurantTableModel:
    table = RestaurantTableModel.query.get(table_id)

    if table:
        return table.serialize(), HTTPStatus.OK

    return {"status": "table not found!"}, HTTPStatus.NOT_FOUND


def get_tables() -> dict:
    args = request.args
    response = []

    if "empty" in args:
        empty = args["empty"]
        query = RestaurantTableModel.query.filter_by(empty=empty).all()
        response += query

        list = []
        for table in response:
            list.append(table.serialize())

        return list

    return get_all()
