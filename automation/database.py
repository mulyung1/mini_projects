from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from icecream import ic


DATABASE_URL = os.getenv('DATABASE_URL')
ic(DATABASE_URL)
Base =  DeclarativeBase()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#defint your data models
class Provider(Base):
    __tablename__ = 'providers'
    
    id = Column(Integer, primary_key=True)
    name = Columns(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    location = Column(String(50), nullable=False, unique=True)

class Products(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Columns(String(50), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    provider_id = Column(Integer, nullable=False)

