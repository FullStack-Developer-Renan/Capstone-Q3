from app.models.users_model import UsersModel
from flask import jsonify, request
from flask_restful import reqparse
from app.services.helpers import add_commit


def get_all():

    args = request.args
    response = []

    if "cpf" in args and "name" not in args:
        cpf = args['cpf']
        query = UsersModel.query.filter_by(cpf=cpf).all()
        response.append(query)

    if "name" in args and "cpf" not in args:
        name = args['name']
        query = UsersModel.query.filter_by(name=name).first()
        response += query

    if "name" and "cpf" in args:
        name = args['name']
        cpf = args['cpf']
        query = UsersModel.query.filter_by(name=name, cpf=cpf).fist()
        response += query

    list_optional_atr = []

    for value in response:
        list_optional_atr.append(value.serialize())

    from ipdb import set_trace
    set_trace()
    return list_optional_atr


def get_user(user_cpf: str) -> dict:
    user = UsersModel()
    query = user.query.filter_by(cpf=user_cpf).first()
    return {"id": query.id, "name": query.name, "cpf": query.cpf}


def create_user():
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True)
    parser.add_argument("cpf", type=str, required=True)

    new_user = UsersModel(**parser.parse_args(strict=True))
    add_commit(new_user)
    return {"id": new_user.id, "name": new_user.name, "cpf": new_user.cpf}


def update_user(id: int, data: dict) -> dict:
    user = UsersModel()
    query = user.query.get(id)

    for key, value in data.items():
        setattr(query, key, value)

    add_commit(query)
    return query
