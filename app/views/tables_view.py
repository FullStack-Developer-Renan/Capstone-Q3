from flask_restful import Resource
from http import HTTPStatus


from app.services.tables_services import get_by_id, create_table


class TablesResource(Resource):
    def get():
        return ...
