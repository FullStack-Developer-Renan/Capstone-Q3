from app.models.orders_model import OrdersModel
from app.models.restaurant_table_model import RestaurantTableModel
from app.services.helpers import add_commit, delete_commit
from flask import jsonify
from http import HTTPStatus
from ipdb import set_trace ## retirar

from flask_restful import reqparse

def create_order():     ## OK
    parser = reqparse.RequestParser()
    
    parser.add_argument("table_id",type = int, required=True)
    parser.add_argument("date", type = str, required=True)
    parser.add_argument("estimated_arrival", type = str)
    parser.add_argument("cooking", type = bool)
    parser.add_argument("ready", type = bool)
    parser.add_argument("delivered", type = bool)
    parser.add_argument("paid", type = bool)


    # arguments = parser.parse_args()
    # order = OrdersModel(**arguments)

    order: OrdersModel = OrdersModel(**parser.parse_args())

    
    add_commit(order)

    return jsonify(order), HTTPStatus.CREATED

def get_current_orders(cooking: bool,ready: bool,delivered: bool) -> dict:
    cooking = eval(cooking) if cooking else False
    ready = eval(ready) if ready else False
    delivered = eval(delivered) if delivered else False

    order = OrdersModel()
    query = order.query.filter(order.cooking == cooking,order.ready == ready,order.delivered == delivered).all()

    return query, HTTPStatus.OK

def get_order_by_table(table_id: int,cooking: bool,ready: bool,delivered: bool) -> dict:
    cooking = eval(cooking) if cooking else False
    ready = eval(ready) if ready else False
    delivered = eval(delivered) if delivered else False

    order = OrdersModel, HTTPStatus.OK

    joined_tables = order.query(
         RestaurantTableModel
        ).select_from(
            OrdersModel
        ).filter(
            RestaurantTableModel.id == OrdersModel.table_id,OrdersModel.table_id == int(table_id)
        ).all()


    return joined_tables, HTTPStatus.OK

def get_orders() -> list[OrdersModel]: ## ok
    users_list: list[OrdersModel] = OrdersModel.query.all()
    return jsonify(users_list), HTTPStatus.OK


def get_order(order_id: str) -> dict: ##ok
    order = OrdersModel()
    query = order.query.get(order_id)
    return query, HTTPStatus.OK

def remove_order(id:int) -> None: ##ok

    order = OrdersModel()
    query = order.query.get(id)
    delete_commit(query)

    return {"message": "Order Deleted!"}, HTTPStatus.NO_CONTENT


def update_order(id: int, data: dict) -> dict:
    order = OrdersModel()
    query = order.query.get(id)

    for key, value in data.items():
        setattr(query, key, value)

    add_commit(query)
    return query, HTTPStatus.OK
