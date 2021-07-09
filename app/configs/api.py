
from flask import Flask
from flask_restful import Api

def init_app(app: Flask) -> None:
    api = Api(app)
    
    
    from app.models.users_model import UsersModel
    from app.models.restaurant_table_model import RestaurantTableModel
    from app.models.orders_model import OrdersModel
    from app.models.products_model import ProductsModel
    from app.models.products_orders_model import ProductsOrdersModel
    
    from app.views.products_view import ProductsResource
    api.add_resource(ProductsResource, '/api/products', endpoint='PRODUCTS')
    from app.views.users_view import UsersResource, UserIdResource
    api.add_resource(UsersResource, '/api/users', endpoint='USERS')
    api.add_resource(UsersResource, '/api/users/<int:id>', endpoint='USERS/')
    # api.add_resource(productIDResource, '/api/products/<int:product_id>', endpoint='product')
