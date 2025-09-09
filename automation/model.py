from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

#defint your data models
class Provider(DeclarativeBase):
    __tablename__ = 'providers'
    
    id = Column(Integer, primary_key=True)
    name = Columns(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    location = Column(String(50), nullable=False, unique=True)

