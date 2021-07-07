from app.models.orders_model import OrdersModel
from app.models.restaurant_table_model import RestaurantTableModel
from app.services.helpers import add_commit, delete_commit
from flask import jsonify

from flask_restful import reqparse

def create_order():
    parser = reqparse.RequestParser()
    
    parser.add_argument("table_id",type = int, required=True)
    parser.add_argument("date", type = str, required=True)
    parser.add_argument("estimated_arrival", type = str)
    parser.add_argument("cooking", type = bool)
    parser.add_argument("ready", type = bool)
    parser.add_argument("delivered", type = bool)
    parser.add_argument("paid", type = bool)

    arguments = parser.parse_args(strict=True)

    order = OrdersModel(**arguments)

    add_commit(order)

    return order

def get_current_orders(cooking: bool,ready: bool,delivered: bool) -> dict:
    cooking = eval(cooking) if cooking else False
    ready = eval(ready) if ready else False
    delivered = eval(delivered) if delivered else False

    order = OrdersModel()
    query = order.query.filter(order.cooking == cooking,order.ready == ready,order.delivered == delivered).all()

    return query

def get_order_by_table(table_id: int,cooking: bool,ready: bool,delivered: bool) -> dict:
    cooking = eval(cooking) if cooking else False
    ready = eval(ready) if ready else False
    delivered = eval(delivered) if delivered else False

    order = OrdersModel

    joined_tables = order.query(
         RestaurantTableModel
        ).select_from(
            OrdersModel
        ).filter(
            RestaurantTableModel.id == OrdersModel.table_id,OrdersModel.table_id == int(table_id)
        ).all()


    return joined_tables

def get_orders() -> list[OrdersModel]:
    users_list: list[OrdersModel] = OrdersModel.query.all()
    return jsonify(users_list)


def get_order(order_id: str) -> dict:
    order = OrdersModel()
    query = order.query.get(order_id)
    return query

def remove_order(id:int) -> None:

    order = OrdersModel()
    query = order.query.get(id)
    delete_commit(query)

    return ""

def update_order(id: int, data: dict) -> dict:
    order = OrdersModel()
    query = order.query.get(id)

    for key, value in data.items():
        setattr(query, key, value)

    add_commit(query)
    return query
