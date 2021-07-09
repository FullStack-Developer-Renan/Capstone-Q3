from app.models.users_model import UsersModel
from flask import jsonify
from flask_restful import reqparse
from .helpers import add_commit


def get_all() -> list[UsersModel]:
    users_list: list[UsersModel] = UsersModel.query.all()
    return jsonify(users_list)


def get_user(user_cpf: str) -> dict:
    user = UsersModel()
    query = user.query.get(user_cpf)
    return query


def create_user(data) -> dict:
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True)
    parser.add_argument("cpf", type=str, required=True)

    new_user = UsersModel(**data)
    add_commit(new_user)
    return new_user


def update_user(id: int, data: dict) -> dict:
    user = UsersModel()
    query = user.query.get(id)

    for key, value in data.items():
        setattr(query, key, value)

    add_commit(query)
    return query
