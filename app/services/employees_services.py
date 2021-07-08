from app.models.employees_model import EmployeesModel
from flask import jsonify, current_app
from flask_restful import reqparse
from http import HTTPStatus

from app.services.helpers import add_commit


def get_all() -> list[EmployeesModel]:
    employees_list: list[EmployeesModel] = EmployeesModel.query.all()
    return jsonify(employees_list), HTTPStatus.OK

def get_by_id(id) -> EmployeesModel:
    employee = EmployeesModel.query.get(id)
    if employee:
        return employee, HTTPStatus.OK
    return {}, HTTPStatus.NOT_FOUND


def create_employee() -> EmployeesModel:
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True)
    parser.add_argument("login", type=str, required=True)
    parser.add_argument("cpf", type=str, required=True)
    parser.add_argument("is_admin", type=bool, required=False)
    parser.add_argument("password", type=str, required=True)

    password = parser.pop('password')
    new_employee: EmployeesModel = EmployeesModel(**parser.parse_args(strict=True))
    new_employee.password = password

    add_commit(new_employee)

    return new_employee


def update_employee(id) -> EmployeesModel:
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=False)
    parser.add_argument("login", type=str, required=False)
    parser.add_argument("cpf", type=str, required=False)
    parser.add_argument("is_admin", type=bool, required=False)
    parser.add_argument("password", type=str, required=False)

    employee = get_by_id(id)
    if not employee:
        return {}, HTTPStatus.NOT_FOUND
    
    for key, value in parser.parse_args(strict=True):
        setattr(employee, key, value)
    
    add_commit(employee)

    return employee, HTTPStatus.OK

def delete_employee(id) -> str:
    session = current_app.db.session

    employee = EmployeesModel.query.get(id)

    session.delete(employee)
    session.commit()

    return "", HTTPStatus.NO_CONTENT



