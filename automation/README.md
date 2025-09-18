# Automation

## objectives
- create a database for the stations
- insert data into the database


## create a database
1. install sqlalchemy and psycopg2
```bash
pip install sqlalchemy psycopg2 python-dotenv
```
2. create a database.py file that has your database models


```python
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

```
3. create the database
```sql
CREATE DATABASE automation;
```
4. create a .env file that has your database url
```DATABASE_URL=postgresql://username:password@localhost:5432/automation
```
5. create an insert.py file that will insert data into the database
the insert file will
- create a database engine(the connection to the database)
- create a sessionmaker that allows us to interact with the database
- get a session
- insert a new provider and product

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from icecream import ic
from database import Base, Provider, Products
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
ic(DATABASE_URL)

#1. create the database engine
engine = create_engine(DATABASE_URL)


#2. create the database tables
Base.metadata.create_all(engine)

#3. create a session using SQLAlchemy’s
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#4. get a session
def get_db():
    return SessionLocal()



if __name__ == '__main__':
    #get a database session
    session = get_db()

    #insert a new provider and product
    try:
        new_provider = Provider(name='Provider1', email='eBt3l@example.com', location='location1')
        new_product = Products(name='Product1', price=100, provider_id=1)
        session.add(new_provider)
        session.add(new_product)
        session.commit()
        ic('Inserted new provider and product')
    except Exception as e:
        ic(f'Error inserting data: {e}')
        session.rollback()
    finally:
        session.close()

```
6. run the insert.py file
```bash
python insert.py
```
if all goes well you should see the message "Inserted new provider and product"

