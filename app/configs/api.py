from flask import Flask
from flask_restful import Api

def init_app(app: Flask) -> None:
    api = Api(app)
    
    
    from app.models.users_model import UsersModel
    from app.models.restaurant_table_model import RestaurantTableModel
    from app.models.orders_model import OrdersModel
    from app.models.products_model import ProductsModel
    from app.models.products_orders_model import ProductsOrdersModel
    
    from app.views.employees_view import EmployeesResource, EmployeeIDResource

    api.add_resource(EmployeesResource, '/api/employees', endpoint='EMPLOYEES')
    api.add_resource(EmployeeIDResource, '/api/employees/<int:employee_id>', endpoint='EMPLOYEE')
