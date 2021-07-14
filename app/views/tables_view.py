from flask_restful import Resource
from http import HTTPStatus


from app.services.tables_services import (
    get_tables,
    create_table,
    get_by_id,
    delete_table,
    login_table,
    update_table,
)


class TablesResource(Resource):
    def get(self):
        return get_tables()

    def post(self):
        return create_table()


class TableIdResource(Resource):
    def get(self, id: int):
        return get_by_id(id)

    def delete(self, id: int):
        return delete_table(id)

    def patch(self, id: int):
        return update_table(id)


class TableLoginResource(Resource):
    def post(self):
        return login_table()
