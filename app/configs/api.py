from flask import Flask
from flask_restful import Api

def init_app(app: Flask) -> None:
    api = Api(app)
    
    from app.models.employees_model import EmployeesModel # Apenas para flask migrate / remover quando criar a view