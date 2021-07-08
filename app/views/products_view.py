from flask_restful import Resource
from http import HTTPStatus

from app.services.products_services import get_by_id, update_product, create_product, delete_product

class ProductsResource(Resource):
    # def get():
    #     return get_all()
    
    def post(self):
        return create_product()

class ProductIDResource(Resource):
    def get(self, product_id: int): 
        return get_by_id(product_id)

    def patch(self, product_id: int):
        return update_product(product_id)

    def delete(self, product_id: int):
        return delete_product(product_id)

