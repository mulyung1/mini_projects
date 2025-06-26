from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status, Request, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from passlib.context import CryptContext
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Users
from fastapi.middleware.cors import CORSMiddleware
#load environment variables from the .env file
load_dotenv()


# to get a secure secret key string run:
# openssl rand -hex 32
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES =int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))


# Create a database session
engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


"""#function to read user details from env file
def load_users_from_env() -> dict:
    #insist on dictionary to support pydantic validation against user model
    users={}
    for user_key in ["VICTOR", "ALEX"]:
        username=os.getenv(f"USER_{user_key}_USERNAME")
        if username:
            users[username]={
                "username":username,
                "full_name":os.getenv(f'USER_{user_key}_FULLNAME'),
                "email":os.getenv(f'USER_{user_key}_EMAIL'),
                "hashed_password":os.getenv(f'USER_{user_key}_HASHED_PASSWORD'),
                "disabled":os.getenv(f'USER_{user_key}_DISABLED')
            }
    return users

#initialise the users db
users_db = load_users_from_env()"""

def load_users_from_db():
    db = SessionLocal()
    try:
        return db.query(Users).all()
    finally:
        db.close()

users_db=load_users_from_db()


#used for the response from in token endpoint
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Add CORS middleware (still needed even with Nginx CORS)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


#utility function to verify the password
def verify_password(plain_password, hashed_password):
    print(f'plain_password {plain_password}')
    return pwd_context.verify(plain_password, hashed_password)

#utility function to hash passwords
def get_password_hash(password):
    return pwd_context.hash(password)

#utility function to get the users from db.
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)

def get_user(username: str):
    user = next((user for user in users_db if user.username == username), None)
    
    if user:
        return UserInDB(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            hashed_password=user.hashed_password,
            disabled=user.disabled,
        )
    raise HTTPException(status_code=404, detail="User not found")

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
        time_now=datetime.now(timezone.utc)
        print(f'time now: {time_now}')
        expire = time_now + expires_delta
        print(f'expiration time: {expire}')
    # else:
    #     expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    print(f'to encode: {to_encode}')
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(encoded_jwt)
    return encoded_jwt

#get current user from the token
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=[ALGORITHM]
        )
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
        raise credentials_exception
        
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)],):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# @app.post("/register/")
# async def register_user(user: User, password: str = Body(...)):
#     if user.username in users_db:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Username already registered",
#         )

#     # Hash the password
#     hashed_password = get_password_hash(password)

#     # Store the new user in the fake database
#     users_db[user.username] = {
#         "username": user.username,
#         "full_name": user.full_name,
#         "email": user.email,
#         "hashed_password": hashed_password,
#         "disabled": False,
#     }

#     return {"message": "User registered successfully"}, users_db

@app.get("/")
async def landing_page()-> dict:
    content={"Salut!":"Welcome Home", "Tip":"Navigate to http://127.0.0.1:8000/docs"}
    return content

from fastapi import Response

@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(seconds=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    
    response = {'access_token':access_token, 'token_type':"bearer"}
    return Response(content=json.dumps(response), media_type="application/json", headers={"Access-Control-Allow-Origin": "*"})

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: Annotated[User, Depends(get_current_active_user)]):
    return [{"item_id": "Foo", "owner": current_user.username}]

@app.get("/home", response_class=HTMLResponse)
async def read_root(request: Request, user: Annotated[User,Depends(get_current_active_user)]):
    return templates.TemplateResponse("index.html", {"request": request, "message": "World"})
