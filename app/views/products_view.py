from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus
from sqlalchemy.exc import DataError
from sqlalchemy.orm.exc import UnmappedInstanceError

# from ipdb import set_trace
from flask import request

from app.services.products_services import (
    get_all,
    get_by_id,
    update_product,
    create_product,
    delete_product,
)


class ProductsResource(Resource):
    def get(self):
        try:
            return get_all(), HTTPStatus.OK
        except DataError as _:
            return {"Message": "Invalid parameter value!"}, HTTPStatus.UNPROCESSABLE_ENTITY

    def post(self):
        return create_product(), HTTPStatus.CREATED


class ProductIDResource(Resource):
    def get(self, product_id: int):
        return get_by_id(product_id)

    def patch(self, product_id: int):
        try:
            return update_product(product_id)
        except TypeError as _:
            return {"error":"Product doesn't exists"}, HTTPStatus.NOT_FOUND

    def delete(self, product_id: int):
        try:
            return delete_product(product_id)

        except UnmappedInstanceError as _:
            return {"error": "produto não existe"}, HTTPStatus.UNPROCESSABLE_ENTITY
