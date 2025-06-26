# Set up Authentication System on FastAPI 
[source](https://fastapi.tiangolo.com/tutorial/security/)

- In this project, we will set up an authentication system, protecting an endpoint that reads user data from a SQLite database, for authenticated in users.
- Imagine your **backend** API is in some domain.
- And your **frontend** is in another domain or
    - in a different path of the same domain or
    - in a mobile app. 
- And you want to have a way for the frontend to authenticate with the backend, using a **username**, **password** and **Token**.
- We can use **OAuth2** to build that with **FastAPI**.
- We use the tools provided by FastAPI to handle security.
## Step 1: Set up working env
- In your working directory, create and activate your virtual env
```
#create a venv
python3 -m venv venv

#activate the venv
source venv/bin/activate
```
  
- install the fast api package and uvicorn to serve your app.
```
pip install fastapi[standard] uvicorn[standard]
```
- `fastapi[standard]` automatically installs the `python-multipart package`
- This is useful as **OAuth2** uses "form data" for sending the `username` and `password`.
### Step 2: Create a basic fastapi app.
------------------------------------------------------------------------
Copy this code to `main.py`
```Python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me/")
async def read_users_me():
	return {"Hello": "world"}
```
### Step 3: Add authorise button.
------------------------------------------------------------------------
- FastAPI provides numerous tools for security. 
- Our authentication system will make use of OAuth2, with the **password** flow using a **Bearer** token.
- FastAPI has a class, `OAuth2PasswordBearer`, that implements this. 
- Let's import the class from `fastapi.security`
```Python
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
```
- When we instantiate this class, we pass a parameter `tokenUrl`
```Python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```
- This parameter contains the URL the client will use to send the `username` and `password` to get a `token` (as per the OAuth2 specification).
- The class is responsible for our authorise button, when it's instance is added(injected) as a dependency to our `/users/me/` endpoint. 
- This dependency provides a `str` that is assigned to the parameter `token` in the `read_users_me` function. 
- Import `Depends` from `FastAPI` - this will call our dependency(our function with the logic we desire to share)
```Python
from fastapi import Depends
```
- Update the endpoint function to inject our security dependency.
```Python
async def read_users_me(token: Annotated[str, Depends(oauth2_scheme)]):
```
- Let it also return the token value
```
return {"token":token}
``` 
**Question, what is dependency injection(DI)??**
- In programming, this is a way for your code(in this case our endpoint functions) to declare things that it requires in order to work and to use.
- In enforcing security, authentication and role requirements, DI helps us have shared logic (the same code logic again and again) and minimise code repetition.
### Run it
```
uvicorn main:app --reload
```
- Navigate to  http://127.0.0.1:8000/docs in your local browser.
- Voila! you already have a shiny new "Authorise" button.
- Your endpoint too has a little lock in the top-right corner that you can click.
- Clicking on the "Authorize" button, you get yourself a little <u>authorisation form</u>.
- Here you can type a `username` and `password` plus other optional fields. 

| Remember: Even if you type anything in the form, it will not work. We have not implemented that yet! |
| ---------------------------------------------------------------------------------------------------- |
### The Password Flow
------------------------------------------------------------------------
- This is one way to handle security and authentication, defined in OAuth2.
- It is what we will be using in our implementation.
- What happens here anyways?
	- The user types the `username` and `password` in the frontend, and hits `Enter`.
	- The frontend (running in the user's browser) sends that `username` and `password` to a specific URL in our API (declared with `tokenUrl="token"`).
	- The API checks that `username` and `password`, and responds with a "token".
		- A "token" is just a string with some content that we can use later to verify this user.
		- Normally, a token is set to expire after some time.
		    - Why?? So, the user will have to log in again at some point later.
		    - And if the token is stolen, the risk is less. It is not like a permanent key that will work forever (in most of the cases).
	- The frontend stores that token temporarily somewhere.
	- The user clicks in the frontend to go to another section of the frontend web app.
	- The frontend needs to fetch some more data from the API.
		- But it needs authentication for that specific endpoint.
		- So, to authenticate with our API, it sends a header `Authorization` with a value of Bearer plus the token.
		- If the token contains `token-value`, the content of the Authorization header would be: Bearer token-value.


So far, our authentication system,(based on the dependency injection system) gives the endpoint function `token` as a `string`(we cannot see the token yet). 

### Step 4: Create the access token
------------------------------------------------------------------------
- Now, lets create the token that the user will get. 
- It will be a JSON web Token, aka jwt. 
- JWT is a standard to codify a JSON object in a long dense string without spaces, like;
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```
- We first install `PyJWT`
```Python
pip install pyjwt
```
- Create a random secret key that will be used to sign the JWT tokens.
- To generate a secure random secret key use the command:
```Bash
openssl rand -hex 32
```
- Create a `.env` file(add it to your `.gitignore` file) to store;
	- a variable `SECRET_KEY` - copy the output of above comand here.
	- a variable `ALGORITHM` - the algorithm used to sign the JWT token: set it to `"HS256"`.
	- a variable `ACCESS_TOKEN_EXPIRE_MINUTES` - the expiration time of the token.
- Your `.env` file would look like;
```
SECRET_KEY=11edc58a2784b9b5a6dd6deacc6d2f111ab4ab08a3ec06d9b66fd2e9b8830cb9
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
- Import the environment variables in your `main.py` file using `python-dotenv` module.
- For this, 
	- install the module; `pip install python-dotenv`
	- load the environment variables
```Python
from dotenv import load_dotenv
import os

#take environment variables from .env.
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES =int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
```
- Create a utility function to generate a jwt.
- For this, we will encode the username and the expiration time as our claims to the jwt.
- We also set a backup token access expiry time to 15 minutes.
- We will enforce the expiration time later.


```Python
from datetime import datetime, timedelta, timezone
import jwt

#example data to encode: this will be your username
data={"sub":"victor"}

#generate a new access token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.now(timezone.utc) + expires_delta
	else:
		expire = datetime.now(timezone.utc) + timedelta(minutes=15)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	print(f'Token: {encoded_jwt}')
	return encoded_jwt

#call the method to see the token  
create_access_token(data=data)
```

### Step 5: Create the `token`  endpoint
------------------------------------------------------------------------
- We have our token ready, lets create the endpoint that gives this token
- For this we define a Pydantic Model that will be used to validate the token endpoint response(ensure we get a valid token)
```Python
from pydantic import BaseModel

class Token(BaseModel):
	access_token: str
	token_type: str
```
- create the token endpoint
- in this endpoint, we call the `create_token` method, remember to delete the function call from step 4 earlier.
```Python
@app.post("/token")
async def login_for_access_token()-> Token:
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	access_token = create_access_token(data=data,expires_delta=access_token_expires)

	return Token(access_token=access_token, token_type="bearer")
```
- Now we get a response that is an access token that looks like.
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2aWN0b3IiLCJleHAiOjE3MzQ0NDI0MDJ9.QupsetRa436vHc2hUmy4a6Kz6_HBlUShm300KycgkFo",
  "token_type": "bearer"
}
```

- See it is also printed out in the terminal you are serving your app from. 
- Remember the access token is not given to every one, but to the users in our database only(authorised users).
- For our case as well as in the OAuth2 specification, to grant a user an access token, they need to submit their `username` & `password`(we encode this username).
- Where do we get this user data from? From our token endpoint as form data. 
- This is to mean that our token endpoint;
	- depends on the form data to run, and 
	- requires the users in our db. 
- Before we use the form data, we need to first create our database and retrieve user data from it(steps 6 & 7). 
### Step 6: Create the database
------------------------------------------------------------------------
- Install `sqlalchemy`
```Bash
pip install sqlalchemy
```
- Add the db url to a `.env` file(replace `users.db` with yourdesired db name)
```
DATABASE_URL = 'sqlite:///users.db'
```
- create a `database.py` file and add the code below.

```Python

#source = https://medium.com/@sandyjtech/creating-a-database-using-python-and-sqlalchemy-422b7ba39d7e
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the database URL from environment variables
database_url = os.getenv("DATABASE_URL")

# Create a database engine for connecting to the database
engine = create_engine(database_url)

# Define a base class for database models
Base = declarative_base()

# Define a Users model representing a table in the database
class Users(Base):
    __tablename__ = "users"  # Table name in the database

    # Define columns with data types and constraints
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    username = Column(String, unique=True, index=True)  
    full_name = Column(String)  
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) 
    disabled = Column(Boolean, default=False)  

# Create the database table based on the model defined above
Base.metadata.create_all(engine)

# Create a session for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user instance with specific data
new_user = Users(
    id=2,  # Unique ID for the user
    username='alex',  # Username for login
    full_name='Alex Kasai',  # Full name of the user
    email='alex@gmail.com',  # User's email address
    hashed_password='$2b$12$c5g7ZUHAdOInIKYNSRMxj.osA4dpdcd03cfQN0RXa5sBuiGM1xR2y',  # Pre-hashed password
    disabled=False  # Ensure the account is active
)

# Uncomment the line below to add the new user to the session
# session.add(new_user)

# Commit the changes to the database
session.commit()

# Query all users from the database
all_users = session.query(Users).all()
# Uncomment the line below to print all users
# print(all_users)

# Query a specific user by username
user = session.query(Users).filter_by(username='victor').first()
# Uncomment the line below to print the user details
# print(user)

# Close the session after completing database operations
session.close()

```

- Run it to:
	- create our db and populate it with new users(un-comment line **`50`** to add a new user). 
	- After populating your db, comment line 50 again to avoid conflicting insertions due to fastapi's use of `watchfiles`
- Also, edit the `new_user` variable for your new users

- To hash your passwords, run this code(see in step 10 also);
  - replace `'password'` with your intended password.
```
from passlib.context import CryptContext

#create a password context
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

#print out the hashed password
print(pwd_context.hash('password'))
```



### Step 7: Get the user data from the db
------------------------------------------------------------------------
 - Now, we get the user data from the database.
 
- create a db session
```Python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#create a database session
engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```
- Create a utility function to fetch users from the db
```Python
from database import Users


def load_users_from_db():
	db = SessionLocal()
	try:
		return db.query(Users).all()
	finally:
		db.close()
#store the users in a variable users_db		
users_db=load_users_from_db()
```
- Now that our users are stored in the `users_db` variable, we can refer to the variable every time we want the user data.
- We now create a utility function `get_user` to actually do the retrieving and return the validated user data, and  if user is not in db we return a HTTP error, using `HTTPException` from fastapi.
```Python
from fastapi import HTTPException
```
- To validate this data, we need a pydantic class to insist that the data we get from the db, is of the defined types in the class. 
```Python

class User(BaseModel):
	username: str
	email: str | None = None
	full_name: str | None = None
	disabled: bool | None = None


	
def get_user(username: str):
	user = next((user for user in users_db if user.username == username), None)
	if user:
		user_dict = {
            "username": user.username,
            "full_name": user.full_name,
            "email": user.email,
            "disabled": user.disabled,
        }
		return User(**user_dict)
	raise HTTPException(status_code=404, detail="User not found")
```
- Now that we have our user data ready, we can check if its available from our `/users/me` endpoint.
- Call the `get_user` method in this endpoint and supply a username found in your db.
- Your endpoint now looks like;
```
@app.get("/users/me/")
async def read_users_me(token: Annotated[str, Depends(oauth2_scheme)]):
	user=get_user('victor')
	return {"user data":user}
```
- Executing this endpointr will return `401 Unauthorized`.
- Why you ask, we have not yet authenticated to access the endpoint.
### Step 8: Get username and password from form data
------------------------------------------------------------------------
- Import `OAuth2PasswordRequestForm`, and use it as a dependency with `Depends` in the _path operation_ for `/token`.
- add this to your code(edit your `/token` endpoint).
```Python
from fastapi.security import OAuth2PasswordRequestForm

async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()])-> Token:
```
- `OAuth2PasswordRequestForm` is a class dependency that declares a form body with:
	- Required:
		- `username`.
		- `password`.
	- Optional:
		- `scope` field as a big string, composed of strings separated by spaces.
		- `grant_type`, `client_id` & `client_secret` fields(not needed in our example).
- It automatically extracts the form data from the login request.
- Instead of passing credentials directly, the credentials are accessed from `form_data`
- What are the credentials(`form_data`) used for?
### Step 9: Use the form data to authenticate user and create a JWT
------------------------------------------------------------------------
- We now check if this user trying to access our api is in the db and create an access token.
- By cross checking the `form_data` against our db records.
- We define a utility function that does the checking(authentication).
```Python
#utility function to check if user is in db
def authenticate_user(users_db, username: str, password: str):
	user = get_user(username)
	if not user:
		return False
	return user
```
- At this level, It does not matter the password used, but if the user is found, an access token is given. 
- Import `status` from fastapi
```Python
from fastapi import status
``` 
- Use our `authenticate_user` function inside our token endpoint.
- If user in form data does not exist in our db, we return an error saying "Incorrect username".
	- For the error, we use `HTTPException`:
```Python
user = authenticate_user(users_db, form_data.username, form_data.password)
if not user:
	raise HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Incorrect username",
		headers={"WWW-Authenticate": "Bearer"},
	)
```
- Now that the user is in our db, we create a token with this returned value.
- This is done by replacing the `data` dictionary used to encode our jwt in step 4 with the form data like so:
```
access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
```

__Tip: Remember to delete the data dictionary in step 4__

#### Password Hashing
------------------------------------------------------------------------
- So far, our system has two levels(JWT and verified username) of security.
- That is, if user is in db, they get an access token, regardless of their password being correct or not. 
- We now add an extra layer of security, the password. 
	- This is where we use the password argument in our `authenticate_user` function.
	- This password has to first be **<u>verified</u>**, thus define a utility function to do this.
- But what if we loose our db to a hacker, we need to ensure that even then we don't give the hacker full access to our system.
	- For this, we **<u>hash</u>** our passwords.
	- This means that we convert the passwords to a sequence of bytes(just a string) that looks like gibberish.
	- Whenever you pass exactly the same content (exactly the same password) you get exactly the same gibberish.
- The advantage is that the hacker will not be able to convert from the gibberish back to the password.
- Run the `hashing.py` code below to hash your passwords
	- Replace `'password'` with your intended password
```Python
from passlib.context import CryptContext

#create a password context
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

#print out the hashed password
print(pwd_context.hash('password'))

```

### Step 10: Hash and Verify passwords
------------------------------------------------------------------------
- Install `passlib`
```Bash
pip install passlib[bcrypt]
```
- PassLib is a great Python package to handle password hashes.
- It supports many secure hashing algorithms and utilities to work with them
- The recommended algorithm is "Bcrypt".
- Import the tools we need from `passlib`.
```Python
from passlib.context import CryptContext
```
- Create a PassLib "context". This is what will be used to hash and verify passwords.
```Python
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
```
- Create a utility function to hash a password coming from the user.
```Python
#utility function to hash passwords
def get_password_hash(password):
	return pwd_context.hash(password)
```
- Create another utility to verify if a received password matches the hash stored.
```Python
#utility function to verify the password
def verify_password(plain_password, hashed_password):
	return pwd_context.verify(plain_password, hashed_password)
```
- But we need to first retrieve the hashed password.
	- For this, we define a pydantic model(`UserInDB`) defining our hashed password type.
	- This model will inherit from the `User` model that validates the fetched user in the `get_user` function.
```
#inherits from User
class UserInDB(User):
	hashed_password: str
``` 

   - We update the user dictionary in the `get_user` function to fetch the hashed password too for verification, and returning the `UserInDB` model instead of `User`.

```
user_dict = {
	"username": user.username,
	"full_name": user.full_name,
	"email": user.email,
	"hashed_password": user.hashed_password,
	"disabled": user.disabled,
}
	return UserInDB(**user_dict)
```

- update the `authenticate_user` utility function to verify the password
```Python
if not verify_password(password, user.hashed_password):
	return False
```
- update the token endpoint to return a message for incorrect passwords
```Python
detail="Incorrect username or password",
```
### Use Token data
------------------------------------------------------------------------
- Till now, our authentication system is set with three layers of security.
- Our `read_users_me` endpoint is reading user details for a user supplied we manually.
- Let us now get the user details, from the db by using the data we encoded in our jwt.
- This makes the code dynamic, in that it will give us the details for the user who just received a jwt(the current user).
- This is where we enforce the token expiration time and really secure our system. 
- We will define a `get_current_user` utility function, that;
  - Extracts username from jwt
  - Uses that username to query user details in db.
  - If the token expiration time is reached, we raise an HTTP error and prompt the user to `Authorize` again(get another access token).

- Lets import the tools to check expiration and validate the token
```
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError 
```

- To get the user details, the `get_current_user` function will require a token that bears the token data.
- Therefore our function depends on the token wich is stored in the `token` url supplied by our security scheme, `oauth2_scheme` object.

- Let's create a pydantic class to define the token data(current users username) we receive is of type str.
```
class TokenData(BaseModel):
	username: str | None = None
```
- The token data 
- Let's now define the method.
```
#get current user from the token
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_exp":True})
		print(f"payload(decoded jwt): {payload}")
		username: str = payload.get("sub")
		if username is None:
			raise credentials_exception
		token_data = TokenData(username=username)
	except ExpiredSignatureError:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Token is expired! Hit Authorize to receive a new token",
			headers={"WWW-Authenticate": "Bearer"},
		)
	except InvalidTokenError:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Could not validate token",
			headers={"WWW-Authenticate": "Bearer"},
		)
	user=get_user(username=token_data.username)
	if user is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User not found in token data",
			headers={"WWW-Authenticate": "Bearer"},
		)
	return user
```

- Our `users/me/` endpoint function(`read_users_me`)  now needs to be updated to be dynamic.
- It depends on the `get_current_user` function to fetch user details.
- It will look like;

```
@app.get("/users/me/")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
	return {"user data":current_user}
```

- To test the expiration time of the token, set the `timedelta` argument of the `access_token_expires` variable in the `token` endpoint to `seconds` instead of `minutes` and watch.

The code now looks something like:
```Python
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
import jwt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Users
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES =int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

# Create a database session
engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_users_from_db():
	db = SessionLocal()
	try:
		return db.query(Users).all()
	finally:
		db.close()
  
users_db=load_users_from_db()

class Token(BaseModel):
	access_token: str
	token_type: str
  
class User(BaseModel):
	username: str
	email: str | None = None
	full_name: str | None = None
	disabled: bool | None = None

class UserInDB(User):
	hashed_password: str

class TokenData(BaseModel):
	username: str | None = None

app = FastAPI()
  
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(username: str):
	user = next((user for user in users_db if user.username == username), None)
	if user:
		user_dict = {
			"username": user.username,
			"full_name": user.full_name,
			"email": user.email,
			"hashed_password": user.hashed_password,
			"disabled": user.disabled,
		}
		return UserInDB(**user_dict)
	raise HTTPException(status_code=404, detail="User not found in db")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#utility function to hash passwords
def get_password_hash(password):
	return pwd_context.hash(password)

#utility function to verify the password
def verify_password(plain_password, hashed_password):
	return pwd_context.verify(plain_password, hashed_password)

#utility function to authenticate user
def authenticate_user(users_db, username: str, password: str):
	user = get_user(username)
	if not user:
		return False
	if not verify_password(password, user.hashed_password):
		return False
	return user

#generate a new access token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.now(timezone.utc) + expires_delta
	# else:
	# 	expire = datetime.now(timezone.utc) + timedelta(minutes=15)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	print(encoded_jwt)
	return encoded_jwt

#get current user from the token
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_exp":True})
		print(f"payload(decoded jwt): {payload}")
		username: str = payload.get("sub")
		if username is None:
			raise credentials_exception
		token_data = TokenData(username=username)
	except ExpiredSignatureError:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Token is expired! Hit Authorize to receive a new token",
			headers={"WWW-Authenticate": "Bearer"},
		)
	except InvalidTokenError:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Could not validate token",
			headers={"WWW-Authenticate": "Bearer"},
		)
	user=get_user(username=token_data.username)
	if user is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User not found in token data",
			headers={"WWW-Authenticate": "Bearer"},
		)
	return user

#create_access_token(data=data)
@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
	user = authenticate_user(users_db, form_data.username, form_data.password)
	if not user:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Incorrect username or password",
			headers={"WWW-Authenticate": "Bearer"},
		)
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	print(f'access token expiry time: {access_token_expires}')
	access_token = create_access_token(data={"sub":user.username}, expires_delta=access_token_expires)
	return Token(access_token=access_token, token_type="bearer")

  
@app.get("/users/me/")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
	return {"user data":current_user}
```


