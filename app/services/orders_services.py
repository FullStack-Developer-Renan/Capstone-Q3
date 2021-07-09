from app.models.orders_model import OrdersModel
from app.models.restaurant_table_model import RestaurantTableModel
from app.services.helpers import add_commit, delete_commit
from flask.json import jsonify
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

    order: OrdersModel = OrdersModel(**parser.parse_args(strict=True))
    
    add_commit(order)

    return {
        "id":order.id,
        "table_id":order.table_id,
        "date":str(order.date),
        "estimated_arrival":str(order.estimated_arrival),
        "cooking":order.cooking,
        "ready":order.ready,
        "delivered":order.delivered,
        "paid":order.paid,
    }

def get_current_orders(table_id,cooking,ready, delivered) -> dict:
    # cooking = eval(cooking) if cooking else False
    # ready = eval(ready) if ready else False
    # delivered = eval(delivered) if delivered else False

    order = OrdersModel()
    query = order.query.filter(order.table_id == table_id,order.cooking == cooking,order.ready == ready,order.delivered == delivered).all()

    return query, HTTPStatus.OK

def get_orders() -> list[OrdersModel]: ## ok
    orders_list: list[OrdersModel] = OrdersModel.query.all()

    response = []

    for query in orders_list:
            response.append({
            "id":query.id,
            "table_id":query.table_id,
            "date":str(query.date),
            "estimated_arrival":str(query.estimated_arrival),
            "cooking":query.cooking,
            "ready":query.ready,
            "delivered":query.delivered,
            "paid":query.paid,
        })

    return response


def get_order(order_id: int) -> dict: ##ok
    order = OrdersModel()

    query = order.query.get(order_id)

    if query:
        return {
            "id":query.id,
            "table_id":query.table_id,
            "date":str(query.date),
            "estimated_arrival":str(query.estimated_arrival),
            "cooking":query.cooking,
            "ready":query.ready,
            "delivered":query.delivered,
            "paid":query.paid,
        }, HTTPStatus.OK
    
    return {"Message":"Order not found"}, HTTPStatus.NOT_FOUND

def remove_order(id:int) -> None: ##ok

    order = OrdersModel()
    query = order.query.get(id)
    delete_commit(query)

    return ""


def update_order(id: int) -> dict:

    parser = reqparse.RequestParser()
    
    parser.add_argument("table_id",type = int)
    parser.add_argument("date", type = str)
    parser.add_argument("estimated_arrival", type = str)
    parser.add_argument("cooking", type = bool)
    parser.add_argument("ready", type = bool)
    parser.add_argument("delivered", type = bool)
    parser.add_argument("paid", type = bool)

    data = parser.parse_args(strict=True)

    order = OrdersModel()
    query = order.query.get(id)

    for key, value in data.items():
        if value != None:
            setattr(query, key, value)

    add_commit(query)
    return {
        "id":query.id,
        "table_id":query.table_id,
        "date":str(query.date),
        "estimated_arrival":str(query.estimated_arrival),
        "cooking":query.cooking,
        "ready":query.ready,
        "delivered":query.delivered,
        "paid":query.paid,
    }