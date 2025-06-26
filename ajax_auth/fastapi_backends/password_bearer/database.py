
#source: https://medium.com/@sandyjtech/creating-a-database-using-python-and-sqlalchemy-422b7ba39d7e
#Step 1: Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()


#Step 2: Establish a database connection
database_url=os.getenv("DATABASE_URL")
engine=create_engine(database_url)

#Step 3: Define your data model
Base=declarative_base()
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)


#Step 4: Create the database tables
Base.metadata.create_all(engine)

#Step 5: Insert data into the database
Session = sessionmaker(bind=engine)
session = Session()

#Step 6: Adding and creating objects; Inserting a new user into the database
new_user = Users(
    id=2,
    username='alex', 
    full_name='Alex Kasai',
    email='alex@gmail.com', 
    hashed_password='$2b$12$c5g7ZUHAdOInIKYNSRMxj.osA4dpdcd03cfQN0RXa5sBuiGM1xR2y',
    disabled=False
)

#session.add(new_user)
session.commit()

#Step 7: Query data from the database
# Example: Querying all users from the database
all_users = session.query(Users).all()
#print(all_users)

# Example: Querying a specific user by their username
user = session.query(Users).filter_by(username='victor').first()
#print(user)

#Step 8: Close the session
session.close()