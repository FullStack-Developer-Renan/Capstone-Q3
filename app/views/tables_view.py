from flask_restful import Resource
from http import HTTPStatus


from app.services.tables_services import (
    get_all,
    create_table,
    get_table,
    delete_table,
    update_table,
)


class TablesResource(Resource):
    def get(self):
        get_all()

    def post(self):
        return create_table()


class TableIdResource(Resource):
    def get(self, id: str):
        return get_table(id)

    def delete(self, id: str):
        return delete_table(id)

    def patch(self, id: str):
        return update_table(id)
