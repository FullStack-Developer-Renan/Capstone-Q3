from sqlalchemy.sql.sqltypes import Text
from app.models.products_model import ProductsModel
from flask import jsonify, current_app, request
from flask_restful import reqparse
from http import HTTPStatus
from ipdb import set_trace

from app.services.helpers import add_commit


def get_all():
    # /api/products?section=<section:bool>?is_veggie=<is_veggie:bool>
    products_list = []
    # section = request.args.get("section")
    # is_veggie = request.args.get("is_veggie")


    if request.args.get("is_veggie"):
        products_list: list[ProductsModel] = ProductsModel.query.filter_by(is_veggie=request.args.get("is_veggie")).first()


    return products_list

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

    new_product: ProductsModel = ProductsModel(**parser.parse_args())

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

    for key, value in data.items():
        if value != None:
            setattr(query, key, value)

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
    session = current_app.db.session

    product = ProductsModel.query.get(id)

    session.delete(product)
    session.commit()

    return "", HTTPStatus.NO_CONTENT



