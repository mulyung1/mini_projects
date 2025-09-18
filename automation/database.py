from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
Base =  declarative_base()


#define your data models
class Provider(Base):
    __tablename__ = 'providers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    location_name = Column(String(50), nullable=False, unique=True)

class Products(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    provider_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    unit = Column(String(20), nullable=False, default='Litre')

