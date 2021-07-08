from flask_restful import Resource
from http import HTTPStatus

from app.services.employees_services import get_all, get_by_id, update_employee, create_employee, delete_employee

class EmployeesResource(Resource):
    def get():
        return get_all()
    
    def post():
        return create_employee()

class EmployeeIDResource(Resource):
    def get(employee_id: int): 
        return get_by_id(employee_id)

    def patch(employee_id: int):
        return update_employee(employee_id)

    def delete(employee_id: int):
        return delete_employee(employee_id)

