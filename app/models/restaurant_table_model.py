from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db

from sqlalchemy import Column, Integer, Boolean, VARCHAR
from werkzeug.security import generate_password_hash

class RestaurantTableModel(db.Model):
    __tablename__ = "restaurant_tables"

    id = Column(Integer, primary_key=True)

    seats = Column(Integer, default=0)
    number = Column(Integer, nullable=False, unique=True)
    total = Column(Integer, default=0)
    password_hash = Column(VARCHAR, nullable=False)
    empty = Column(Boolean, default=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UsersModel", backref="tables")

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)