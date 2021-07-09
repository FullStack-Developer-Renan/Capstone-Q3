from http import HTTPStatus
from flask_restful import Resource
from ipdb.__main__ import set_trace
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

# class OrdersOptionalsResources(Resource):
#     def get(self, table_id: int, cooking: bool, ready: bool, delivered: bool):
#         args = request.get_json()
#         set_trace()
#         table_id = args["table_id"]
#         cooking = args["cooking"]
#         ready = args["ready"]
#         delivered = args["delivered"]

#         # table_id = request.form["table_id"]
#         # cooking = request.args.get("cooking") if request.args.get("cooking") else False
#         # ready = request.args.get("ready") if request.args.get("ready") else False
#         # delivered = request.args.get("delivered") if request.args.get("delivered") else False

#         set_trace()

#         return get_current_orders(table_id,cooking,ready, delivered)
        
# # table_id=<int:table_id>cooking=<bool:cooking>&ready=<bool:ready>&delivered=<bool:delivered>