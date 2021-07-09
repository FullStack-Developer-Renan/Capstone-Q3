from flask_restful import Resource
from http import HTTPStatus


from app.services.tables_services import get_all, create_table, get_table


class TablesResource(Resource):
    def post(self):
        return create_table()
