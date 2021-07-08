
from flask import Flask
from flask_restful import Api

def init_app(app: Flask) -> None:
    api = Api(app)
    
    
    from app.models.users_model import UsersModel
    from app.models.restaurant_table_model import RestaurantTableModel
    from app.models.orders_model import OrdersModel
    from app.models.products_model import ProductsModel
    from app.models.products_orders_model import ProductsOrdersModel
    from app.models.employees_model import EmployeesModel

    from app.views.orders_views import OrdersResource, OrderIDResource

    api.add_resource(OrdersResource, '/api/orders', endpoint = 'orders')
    api.add_resource(OrderIDResource, "/api/orders/<int:order_id>", endpoint = "order")
    
