from flask import Flask
from flask_restful import Api

def init_app(app: Flask) -> None:
    api = Api(app)
    
    
    from app.models.users_model import UsersModel
    from app.models.restaurant_table_model import RestaurantTableModel
    from app.models.orders_model import OrdersModel
    from app.models.products_orders_model import ProductsOrdersModel
    from app.models.products_model import ProductsModel
    
    from app.views.products_view import ProductsResource, ProductIDResource
    api.add_resource(ProductsResource, '/api/products?is_veggie=<is_veggie: bool>', endpoint='PRODUCTS')
    api.add_resource(ProductIDResource, '/api/products/<int:product_id>', endpoint='PRODUCTS_ID')
