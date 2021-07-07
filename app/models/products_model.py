from sqlalchemy import Column, Integer, String, Boolean
from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass

@dataclass
class ProductsModel(db.Model):
    id: int
    recipe: str
    price: int
    calories: int
    section: str
    is_veggie: bool

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)

    recipe = Column(String(255))
    price = Column(Integer, nullable=False)
    calories = Column(Integer)
    section = Column(String(150))
    is_veggie = Column(Boolean, default=False)
