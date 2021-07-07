from flask import jsonify, request
from .helpers import add_commit
from app.models.restaurant_table_model import RestaurantTableModel
from http import HTTPStatus


def create_table(data: dict):
    new_table = RestaurantTableModel(**data)

    add_commit(new_table)

    return jsonify(new_table)


def delete_table(table_id: int):
    found_table = RestaurantTableModel.query.get(table_id)

    if not found_table:
        return {"status": "table not found"}, HTTPStatus.NOT_FOUND

    add_commit(found_table)

    return "", HTTPStatus.NO_CONTENT


def update_table(data: dict, table_id: int):
       
    found_table = RestaurantTableModel.query.get(table_id)
    
    if not found_table:
        return {"status": "table not found"}, HTTPStatus.NOT_FOUND


    