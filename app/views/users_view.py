from flask_restful import Resource
from http import HTTPStatus
from app.services.users_services import get_all, delete_user, update_user, create_user
from sqlalchemy.exc import DataError
from sqlalchemy.orm.exc import UnmappedInstanceError
from ipdb import set_trace


class UsersResource(Resource):
    def get(self):
        return get_all(), HTTPStatus.OK

    def post(self):
        try:
            return create_user(), HTTPStatus.CREATED
        except DataError as _:
            return {"Message": "Invalid CPF"}, HTTPStatus.UNPROCESSABLE_ENTITY


class UserIdResource(Resource):
    def patch(self, user_id: int):
        try:
            return update_user(user_id), HTTPStatus.OK
        except TypeError as _:
            return {"Message": "User not found"}, HTTPStatus.NOT_FOUND
        except DataError as _:
            return {"Message": "Invalid CPF"}, HTTPStatus.UNPROCESSABLE_ENTITY

    def delete(self, user_id: int):
        try:
            return delete_user(user_id), HTTPStatus.NO_CONTENT
        except TypeError as _:
            return {"Message": "User not found"}, HTTPStatus.NOT_FOUND
        except UnmappedInstanceError as _:
            return {"Message": "User not found"}, HTTPStatus.NOT_FOUND
