from flask import Flask
from flask_restful import Api

def init_app(app: Flask) -> None:
    api = Api(app)
    
    from app.views.employees_view import EmployeesResource, EmployeeIDResource

    api.add_resource(EmployeesResource, '/api/employees', endpoint='EMPLOYEES')
    api.add_resource(EmployeeIDResource, '/api/employees/<int:employee_id>', endpoint='EMPLOYEE')