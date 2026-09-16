from sqlalchemy import Column, Integer, String, Numeric, Boolean
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    color = Column(String(50), nullable=False)
    fabric = Column(String(100), nullable=False)
    work = Column(String(100), nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    available = Column(Boolean, default=True)