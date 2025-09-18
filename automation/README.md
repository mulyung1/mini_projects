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


## Migrartions.
- https://www.kubeblogs.com/build-databases-with-sqlalchemy-and-alembic/

### why alembic?
- **Version Control** alembic records each schema change.
- **safe schema updates** you can apply or undo changes step-wise making schema modificatuons safe.
- **Environment Consistency** your schema remains consistent across different environments(dev, staging, production).

## why SQLAlchemy and Alembic together?
- **simplified data management** data is handled directly with python objects, hence cleaner code.
- **automated migrations** tracking and applying schema changes by alembis ic automatic.
- **scalability** as the project grows, managing complex schemas and relationships becomes easier.

7. install alembic
```bash
pip install alembic
```
8. initialize alembic
- this creates an `alembic/` folder and conf file `alembic.ini`

```bash
alembic init alembic
```
9. configure alembic
- edit alembic.ini to set the sqlalchemy.url to your database url
```ini
sqlalchemy.url = postgresql://username:password@localhost:5432/automation
```
- edit alembic/env.py to import your models and set the target_metadata
```python
from database import Base
target_metadata = Base.metadata
```
10. create a migration script
```bash
alembic revision --autogenerate -m "Initial migration"
```
11. apply the migration
```bash
alembic upgrade head
``` 
if all goes well you will see

![alt text](migration.png)


## Updating the db schema
say you want to add a column in the products table
1. edit the database.py file to add the new column

```python
class Products(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    provider_id = Column(Integer, nullable=False)

    #new columns
    quantity = Column(Integer, nullable=False, default=0)
    unit = Column(String(20), nullable=False, default='Litre')
```
2. create a new migration script
```bash
alembic revision --autogenerate -m "Add quantity and unit to products"
```
3. apply the migration
```bash
alembic upgrade head
``` 
if all goes well you will see

![alt text](update.png)