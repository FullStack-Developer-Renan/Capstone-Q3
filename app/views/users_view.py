from flask_restful import Resource
from http import HTTPStatus
from app.services.users_services import get_all, get_user, update_user, create_user


class UsersResource(Resource):
    def get(self):
        return get_all(), HTTPStatus.OK


class UserIdResource(Resource):
    def get(self, user_cpf: str):
        return get_user(user_cpf), HTTPStatus.OK

    def create(self, data: dict):
        return create_user(data), HTTPStatus.CREATED

    def patch(self, user_id: int, data: dict):
        return update_user(user_id, data), HTTPStatus.OK
