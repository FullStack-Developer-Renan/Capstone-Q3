from flask_restful import Resource
from app.services.orders_services import create_order,get_current_orders,get_order_by_table, get_orders, get_order, remove_order,update_order

class OrdersResource(Resource):
    def post(self):
        return create_order()    
    
    def get(self):
        return get_orders()



class OrderIDResource(Resource):
    def get(self, order_id: int):
        return get_order(order_id)

    def delete(self, order_id: int):
        return remove_order(order_id)
    
    def patch(self, order_id: int):
        return update_order(order_id)