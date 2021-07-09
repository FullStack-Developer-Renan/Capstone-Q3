from flask_restful import Resource
from http import HTTPStatus


from app.services.tables_services import (
    get_all,
    create_table,
    get_by_id,
    delete_table,
    update_table,
)


class TablesResource(Resource):
    def get(self):
        get_all()

    def post(self):
        return create_table()


class TableIdResource(Resource):
    def get(self, id: int):
        return get_by_id(id)

    def delete(self, id: int):
        return delete_table(id)

    def patch(self, id: int):
        return update_table(id)
