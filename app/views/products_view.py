from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.services.products_services import get_all, get_by_id, update_product, create_product, delete_product

class ProductsResource(Resource):
    def get(self):
        return get_all()
    
    def post(self):
        return create_product(), HTTPStatus.CREATED 

class ProductIDResource(Resource):
    def get(self, product_id: int): 
        return get_by_id(product_id)

    def patch(self, product_id: int):
        return update_product(product_id)

    def delete(self, product_id: int):
        try:
            return delete_product(product_id)

        except UnmappedInstanceError as _:
            return {"error": "produto não existe"}, HTTPStatus.UNPROCESSABLE_ENTITY

