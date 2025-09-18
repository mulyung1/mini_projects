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
        new_provider = Provider(name='Shell Ruaraka', email='shellruaraka@gmail.com',latitude=-1.24386, longitude=36.88005, location_name='location1')
        new_product = Products(name='Kerosene', price=169, provider_id=1)
        #session.add(new_provider)
        session.add(new_product)
        session.commit()
        ic('Inserted new provider and product')
    except Exception as e:
        ic(f'Error inserting data: {e}')
        session.rollback()
    finally:
        session.close()