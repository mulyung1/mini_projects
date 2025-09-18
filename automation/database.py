from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base =  declarative_base()


#define your data models
class Provider(Base):
    __tablename__ = 'providers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    location = Column(String(50), nullable=False, unique=True)

class Products(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    provider_id = Column(Integer, nullable=False)

