from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from app.services.tables_services import (
    get_tables,
    create_table,
    get_by_id,
    delete_table,
    login_table,
    update_table,
)


class TablesResource(Resource):
    @jwt_required()
    def get(self):
        return get_tables()

    @jwt_required()
    def post(self):
        return create_table()


class TableIdResource(Resource):
    @jwt_required()
    def get(self, id: int):
        return get_by_id(id)

    @jwt_required()
    def delete(self, id: int):
        return delete_table(id)

    @jwt_required()
    def patch(self, id: int):
        return update_table(id)


class TableLoginResource(Resource):
    def post(self):
        try:
            return login_table()
        except IntegrityError:
            return {"error": "Wrong lenght of parameters"}, HTTPStatus.BAD_REQUEST
