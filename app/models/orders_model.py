from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from sqlalchemy import Integer, Column, Boolean, DateTime
from dataclasses import dataclass


@dataclass
class OrdersModel(db.Model):
    table_id: int
    date: int
    estimated_arrival: int
    cooking: bool
    ready: bool
    delivered: bool
    paid: bool
    products_list: list["ProductsModel"]

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    table_id = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    estimated_arrival = Column(DateTime)
    cooking = Column(Boolean, default=False)
    ready = Column(Boolean, default=False)
    delivered = Column(Boolean, default=False)
    paid = Column(Boolean, default=False)

    # products_list = relationship("ProductsModel", backref=backref("order_list"), secondary="")
