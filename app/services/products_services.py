from app.services.products_orders_services import delete_product_order_by_product
from app.models.products_orders_model import ProductsOrdersModel
from app.models.products_model import ProductsModel
from flask import request
from flask_restful import reqparse
from http import HTTPStatus
from ipdb import set_trace

from app.services.helpers import add_commit, delete_commit

# /api/products?section=<section:bool>?is_veggie=<is_veggie:bool>


def get_all() -> dict:

    args = request.args
    response = []


    if "is_veggie" in args and "price" not in args:
        is_veggie = args["is_veggie"]     
        query = ProductsModel.query.filter_by(is_veggie=is_veggie).all()
        response += query

    if "price" in args and "is_veggie" not in args:
        price = args["price"]
        query = ProductsModel.query.filter_by(price=price).all()
        response += query

    if "price" in args and "is_veggie" in args:
        is_veggie = args["is_veggie"]
        price = args["price"]
        query = ProductsModel.query.filter_by(price=price, is_veggie=is_veggie).all()
        response += query
    
    if "price" not in args and "is_veggie" not in args:
        query = ProductsModel.query.all()
        response += query

    
    list_opcional_atr = []

    for value in response:
        list_opcional_atr.append(value.serialize())

    return list_opcional_atr


def get_by_id(id) -> ProductsModel:
    product = ProductsModel.query.get(id)
    if product:
        return {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "calories": product.calories,
            "section": product.section,
            "is_veggie": product.is_veggie,
        }, HTTPStatus.OK
    return {}, HTTPStatus.NOT_FOUND


def create_product() -> ProductsModel:
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("calories", type=int, required=True)
    parser.add_argument("section", type=str, required=False)
    parser.add_argument("is_veggie", type=bool, required=False)

    args = parser.parse_args(strict=True)

    new_product: ProductsModel = ProductsModel(**args)

    add_commit(new_product)

    return {
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price,
        "calories": new_product.calories,
        "section": new_product.section,
        "is_veggie": new_product.is_veggie,
    }


def update_product(id: int) -> dict:

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("price", type=float)
    parser.add_argument("calories", type=float)
    parser.add_argument("section", type=str)
    parser.add_argument("is_veggie", type=bool)

    data = parser.parse_args(strict=True)

    product = ProductsModel()

    query = product.query.get(id)

    if not query:
        raise("Error")

    for key, valueue in data.items():
        if valueue != None:
            setattr(query, key, valueue)

    add_commit(query)

    return {
        "id": query.id,
        "name": query.name,
        "price": query.price,
        "calories": query.calories,
        "section": query.section,
        "is_veggie": query.is_veggie,
    }


def delete_product(id) -> str:

    product = ProductsModel.query.get(id)

    delete_product_order_by_product(product.id)

    delete_commit(product)

    return "", HTTPStatus.NO_CONTENT


def get_product_by_order_id(order_id):

    products_orders = ProductsOrdersModel.query.filter_by(order_id=order_id).all()

    response = []

    for value in products_orders:
        product = ProductsModel.query.get(value.product_id)
        # serialize = {"name": product.name, "price": product.price}
        response.append(product)

    def remove_repetidos(lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)

        return l

    lista = remove_repetidos(response)
    
    results = []

    for elem in lista:
        quantity = response.count(elem)
        serialize = {"name": elem.name, "price": elem.price, "quantity": quantity}
        results.append(serialize)



    return results
