from app.models.orders_model import OrdersModel
from app.models.products_model import ProductsModel
from app.models.products_orders_model import ProductsOrdersModel as POM
from app.services.helpers import add_commit

def relate_product_order(order_id, product_id): 
    
    order = OrdersModel.query.get(order_id)
    product = ProductsModel.query.get(product_id)

    if order and product:
        product_order = POM(product_id=product.id, order_id=order.id)
    
        add_commit(product_order)


