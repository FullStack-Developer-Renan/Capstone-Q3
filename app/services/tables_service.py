from flask import jsonify
from .helpers import add_commit
from app.models.restaurant_table_model import RestaurantTableModel


def create_table(data: dict) -> dict:
    new_table = RestaurantTableModel(**data)

    add_commit(new_table)

    return jsonify(new_table)
