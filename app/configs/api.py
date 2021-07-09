from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)

    from app.models.users_model import UsersModel
    from app.models.restaurant_table_model import RestaurantTableModel
    from app.models.orders_model import OrdersModel
    from app.models.products_orders_model import ProductsOrdersModel

    from app.views.products_view import ProductsResource, ProductIDResource

    api.add_resource(ProductsResource, "/api/products", endpoint="PRODUCTS")
    api.add_resource(ProductIDResource, '/api/products/<int:product_id>', endpoint='PRODUCTS_ID')
    
    from app.views.users_view import UsersResource, UserIdResource

    api.add_resource(UsersResource, "/api/users", endpoint="USERS")
    api.add_resource(UsersResource, "/api/users/<int:id>", endpoint="USERS/")
    

    from app.views.tables_view import TablesResource, TableIdResource

    api.add_resource(TablesResource, "/api/tables", endpoint="CREATE_TABLE")
    api.add_resource(TableIdResource, "/api/tables/<int:id>", endpoint="TABLES/")
