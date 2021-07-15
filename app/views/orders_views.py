from http import HTTPStatus
from flask_restful import Resource
from ipdb.__main__ import set_trace
from six import reraise
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.sql.expression import table
from flask import request
from sqlalchemy.exc import DataError, IntegrityError
from app.services.orders_services import create_order,get_current_orders, get_orders, get_order, remove_order,update_order
from flask_jwt_extended import jwt_required

class OrdersResource(Resource):
    @jwt_required()
    def post(self):
        try:
            return create_order(),HTTPStatus.CREATED
        except IntegrityError as _:
            return {"Message": "Table_Id doesn't exist"}, HTTPStatus.UNPROCESSABLE_ENTITY
        except DataError as _:
            return {"Message": "Invalid parameter value!"}, HTTPStatus.UNPROCESSABLE_ENTITY
    @jwt_required
    def get(self):
        
        try:
            return get_orders(),HTTPStatus.OK
        except DataError as _:
            return {"Message": "Invalid parameter value!"}, HTTPStatus.UNPROCESSABLE_ENTITY



class OrderIDResource(Resource):
    @jwt_required
    def get(self, order_id: int):
        return get_order(order_id)
        
    @jwt_required
    def delete(self, order_id: int):
        try:
            return remove_order(order_id), HTTPStatus.NO_CONTENT

        except UnmappedInstanceError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.UNPROCESSABLE_ENTITY

        except AttributeError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.UNPROCESSABLE_ENTITY
    
    @jwt_required
    def patch(self, order_id: int):
        try:
            return update_order(order_id), HTTPStatus.CREATED
        
        except UnmappedInstanceError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.UNPROCESSABLE_ENTITY

        except TypeError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.NOT_FOUND
