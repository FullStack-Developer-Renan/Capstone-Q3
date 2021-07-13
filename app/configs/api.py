from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)

    from app.models.users_model import UsersModel
    from app.models.restaurant_table_model import RestaurantTableModel
    from app.models.orders_model import OrdersModel
    from app.models.products_orders_model import ProductsOrdersModel
    from app.models.products_model import ProductsModel
    from app.models.employees_model import EmployeesModel

    from app.views.orders_views import OrdersResource, OrderIDResource
    from app.views.employees_view import EmployeeIDResource, EmployeesResource, EmployeeLoginResource

    api.add_resource(EmployeesResource, "/api/employees", endpoint="EMPLOYEES")
    api.add_resource(EmployeeIDResource, "/api/employees/<int:employee_id>", endpoint="EMPLOYEE_ID")
    api.add_resource(EmployeeLoginResource, "/api/employees/login", endpoint="EMPLOYEE_LOGIN")


    api.add_resource(OrdersResource, "/api/orders", endpoint="ORDERS")
    api.add_resource(OrderIDResource, "/api/orders/<int:order_id>", endpoint="ORDER")

    from app.views.products_view import ProductsResource, ProductIDResource

    api.add_resource(ProductsResource, "/api/products", endpoint="PRODUCTS")
    api.add_resource(
        ProductIDResource, "/api/products/<int:product_id>", endpoint="PRODUCTS_ID"
    )

    from app.views.users_view import UsersResource, UserIdResource

    api.add_resource(UsersResource, "/api/users", endpoint="USERS")
    api.add_resource(UsersResource, "/api/users/<int:id>", endpoint="USER_ID")

    from app.views.tables_view import (
        TablesResource,
        TableIdResource,
        TableLoginResource,
    )

    api.add_resource(TablesResource, "/api/tables", endpoint="TABLE")
    api.add_resource(TableLoginResource, "/api/tables/login", endpoint="TABLE_LOGIN")
    api.add_resource(TableIdResource, "/api/tables/<int:id>", endpoint="TABLES")
