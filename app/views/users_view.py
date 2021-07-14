from flask_restful import Resource
from http import HTTPStatus
from app.services.users_services import get_all, get_user, update_user, create_user
from ipdb import set_trace

class UsersResource(Resource):
    def get(self):
        # set_trace()
        return get_all(), HTTPStatus.OK

    def post(self):
        set_trace()
        return create_user(), HTTPStatus.CREATED


class UserIdResource(Resource):
    def patch(self, user_id: int):
        return update_user(user_id), HTTPStatus.OK
