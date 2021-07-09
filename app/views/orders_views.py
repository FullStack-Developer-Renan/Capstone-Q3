from http import HTTPStatus
from flask_restful import Resource
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.sql.expression import table
from flask import request
from app.services.orders_services import create_order,get_current_orders, get_orders, get_order, remove_order,update_order

class OrdersResource(Resource):
    def post(self):
        return create_order(),HTTPStatus.CREATED 
    
    def get(self):
        return get_orders(),HTTPStatus.OK



class OrderIDResource(Resource):
    def get(self, order_id: int):
        return get_order(order_id)
        
    def delete(self, order_id: int):
        try:
            return remove_order(order_id), HTTPStatus.NO_CONTENT

        except UnmappedInstanceError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.UNPROCESSABLE_ENTITY

        except AttributeError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.UNPROCESSABLE_ENTITY
    
    def patch(self, order_id: int):
        try:
            return update_order(order_id), HTTPStatus.CREATED
        
        except UnmappedInstanceError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.UNPROCESSABLE_ENTITY

class OrdersOptionalsResources(Resource):
    def get(self, table_id, cooking, ready, delivered):
        table_id = int(request.args.get("table_id")) if request.args.get("table_id") else 0
        cooking = eval((request.args.get("cooking")).title()) if eval(request.args.get("cooking")).title() else False
        ready = eval((request.args.get("ready")).title()) if eval(request.args.get("ready")).title() else False
        delivered = eval((request.args.get("delivered")).title()) if eval(request.args.get("delivered")).title() else False

        return get_current_orders(table_id,cooking,ready, delivered)
        
# table_id=<int:table_id>cooking=<bool:cooking>&ready=<bool:ready>&delivered=<bool:delivered>