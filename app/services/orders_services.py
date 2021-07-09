from app.services.products_orders_services import relate_product_order
from sqlalchemy.sql.sqltypes import ARRAY
from app.models.orders_model import OrdersModel
from app.models.restaurant_table_model import RestaurantTableModel
from app.services.helpers import add_commit, delete_commit
from flask.json import jsonify
from http import HTTPStatus
from flask import request
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
    parser.add_argument("products", type = list, location = "json")

    args = parser.parse_args(strict=True)
    
    products = args.pop('products')

    order: OrdersModel = OrdersModel(**args)
    
    add_commit(order)

    for i in products: 
        relate_product_order(order.id, i)

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

def get_current_orders(table_id: int, cooking: bool, ready: bool, delivered: bool) -> dict:

    order = OrdersModel()
    query = order.query.filter(order.table_id == table_id,order.cooking == cooking,order.ready == ready,order.delivered == delivered).all()

    return query, HTTPStatus.OK

def get_orders(): ## ok
    args = request.args
    response = []

    if "table_id" in args and "cooking" not in args and "ready" not in args and "delivered" not in args and "paid" not in args:
        table_id = args["table_id"]
        queries = OrdersModel.query.filter_by(table_id=table_id).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "cooking" in args and "table_id" not in args and "ready" not in args and "delivered" not in args and "paid" not in args:
        cooking = args["cooking"]
        queries = OrdersModel.query.filter_by(cooking=cooking).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query
    
    if "ready" in args and "table_id" not in args and "cooking" not in args and "delivered" not in args and "paid" not in args:
        ready = args["ready"]
        queries = OrdersModel.query.filter_by(ready=ready).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "delivered" in args and "table_id" not in args and "cooking" not in args and "ready" not in args and "paid" not in args:
        delivered = args["delivered"]
        queries = OrdersModel.query.filter_by(delivered=delivered).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query
    
    if "paid" in args and "table_id" not in args and "cooking" not in args and "ready" not in args and "delivered" not in args:
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query
    
    if "delivered" not in args and "table_id" not in args and "cooking" not in args and "ready" not in args and "paid" not in args:

        orders_list: list[OrdersModel] = OrdersModel.query.all()



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

    if "table_id" in args and "cooking" in args and "ready" not in args and "delivered" not in args and "paid" not in args:
        table_id = args["table_id"]
        cooking = args["cooking"]
        queries = OrdersModel.query.filter_by(table_id=table_id, cooking=cooking).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query    
    
    if "table_id" in args and "cooking" not in args and "ready" in args and "delivered" not in args and "paid" not in args:
        table_id = args["table_id"]
        ready = args["ready"]
        queries = OrdersModel.query.filter_by(table_id=table_id, ready = ready).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "table_id" in args and "cooking" not in args and "ready" not in args and "delivered" in args and "paid" not in args:
        table_id = args["table_id"]
        delivered = args["delivered"]
        queries = OrdersModel.query.filter_by(table_id=table_id, delivered = delivered).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query 

    if "cooking" in args and "table_id" not in args and "ready" in args and "delivered" not in args and "paid" not in args:
        cooking = args["cooking"]
        ready = args["ready"]
        queries = OrdersModel.query.filter_by(cooking=cooking, ready=ready).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "cooking" in args and "table_id" not in args and "ready" not in args and "delivered" in args and "paid" not in args:
        cooking = args["cooking"]
        delivered = args["delivered"]
        queries = OrdersModel.query.filter_by(cooking=cooking, delivered=delivered).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "cooking" in args and "table_id" not in args and "ready" not in args and "delivered" not in args and "paid" in args:
        cooking = args["cooking"]
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(cooking=cooking, paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "ready" in args and "table_id" not in args and "cooking" not in args and "delivered" in args and "paid" not in args:
        ready = args["ready"]
        delivered = args["delivered"]
        queries = OrdersModel.query.filter_by(ready=ready, delivered=delivered).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "ready" in args and "table_id" not in args and "cooking" not in args and "delivered" not in args and "paid" in args:
        ready = args["ready"]
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(ready=ready, paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "delivered" in args and "table_id" not in args and "cooking" not in args and "ready" not in args and "paid" in args:
        delivered = args["delivered"]
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(delivered=delivered, paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "paid" in args and "table_id" in args and "cooking" not in args and "ready" not in args and "delivered" not in args:
        paid = args["paid"]
        table_id = args["table_id"]
        queries = OrdersModel.query.filter_by(paid=paid, table_id=table_id).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "table_id" in args and "cooking" in args and "ready" in args and "delivered" not in args and "paid" in args:
        table_id = args["table_id"]
        cooking = args["cooking"]
        ready = args["ready"]
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(table_id=table_id, cooking=cooking,ready=ready, paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "table_id" in args and "cooking" in args and "ready" not in args and "delivered" in args and "paid" in args:
        table_id = args["table_id"]
        cooking = args["cooking"]
        delivered = args["delivered"]
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(table_id=table_id, cooking=cooking, delivered=delivered,paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "table_id" in args and "cooking" not in args and "ready" in args and "delivered" in args and "paid" in args:
        table_id = args["table_id"]
        ready = args["ready"]
        delivered = args["delivered"]
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(table_id=table_id, ready=ready, delivered=delivered,paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "table_id" not in args and "cooking" in args and "ready" in args and "delivered" in args and "paid" in args:
        cooking = args["cooking"]
        ready = args["ready"]
        delivered = args["delivered"]
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(cooking=cooking, ready=ready, delivered=delivered,paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "table_id" in args and "cooking" in args and "ready" in args and "delivered" in args and "paid" not in args:
        table_id = args["table_id"]
        cooking = args["cooking"]
        ready = args["ready"]
        delivered = args["delivered"]
        queries = OrdersModel.query.filter_by(cooking=cooking, ready=ready, delivered=delivered,table_id=table_id).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

    if "table_id" in args and "cooking" in args and "ready" in args and "delivered" in args and "paid" in args:
        table_id = args["table_id"]
        cooking = args["cooking"]
        ready = args["ready"]
        delivered = args["delivered"]
        paid = args["paid"]
        queries = OrdersModel.query.filter_by(table_id=table_id,cooking=cooking, ready=ready, delivered=delivered, paid=paid).all()
        query = []
        for order in queries:
            query.append(order.serialize())
        response += query

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