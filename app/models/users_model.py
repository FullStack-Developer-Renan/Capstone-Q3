from sqlalchemy import Column, Integer, String, Float, ForeignKey
from dataclasses import dataclass


@dataclass
class UsersModel:
    id: int
    cpf: str
    name: str
    total: float

    id = Column(Integer, primary_key=True)
    cpf = Column(String(11), nullable=False, unique=True)
    name = Column(String(150), nullable=False)
    total = Column(Float, default=0)
