from sqlalchemy.sql.sqltypes import Text
from app.models.products_model import ProductsModel
from flask import jsonify, current_app
from flask_restful import reqparse
from http import HTTPStatus

from app.services.helpers import add_commit


# def get_all() -> list[ProductsModel]:
#     products_list: list[ProductsModel] = ProductsModel.query.all()
#     return jsonify(products_list), HTTPStatus.OK

def get_by_id(id) -> ProductsModel:
    product = ProductsModel.query.get(id)
    if product:
        return product, HTTPStatus.OK
    return {}, HTTPStatus.NOT_FOUND


def create_product() -> ProductsModel:
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("calories", type=int, required=True)
    parser.add_argument("section", type=str, required=False)
    parser.add_argument("veggie", type=bool, required=False)

    new_product: ProductsModel = ProductsModel(**parser.parse_args())

    add_commit(new_product)

    return new_product


def update_product(id) -> ProductsModel:
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("calories", type=int, required=True)
    parser.add_argument("section", type=str, required=False)
    parser.add_argument("veggie", type=bool, required=False)

    product = get_by_id(id)
    if not product:
        return {}, HTTPStatus.NOT_FOUND
    
    for key, value in parser.parse_args(strict=True):
        setattr(product, key, value)
    
    add_commit(product)

    return product, HTTPStatus.OK

def delete_product(id) -> str:
    session = current_app.db.session

    product = ProductsModel.query.get(id)

    session.delete(product)
    session.commit()

    return "", HTTPStatus.NO_CONTENT



