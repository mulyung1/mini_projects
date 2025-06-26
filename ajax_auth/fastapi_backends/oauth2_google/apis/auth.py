# auth.py
import os
import uuid
import traceback
from datetime import datetime, timedelta

import requests  # needed for userinfo endpoint
import mysql.connector  # or your preferred MySQL client
from mysql.connector import Error
import logging

from fastapi import FastAPI, Depends, HTTPException, status, Request, Cookie, APIRouter
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from jose import jwt, ExpiredSignatureError, JWTError
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# OAuth Setup
oauth = OAuth()
oauth.register(
    name="auth_demo",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    # The following URLs are standard for Google
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    access_token_url="https://oauth2.googleapis.com/token",
    client_kwargs={"scope": "openid profile email"},
    # jwks_uri is used internally by Authlib to verify id_token
    jwks_uri="https://www.googleapis.com/oauth2/v3/certs",
)

# JWT Configurations for your own token
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

router = APIRouter()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    # Include subject ("sub") as user identifier; data should contain "sub" and "email"
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(access_token: str = Cookie(None)):
    """
    Dependency to get the current user from cookie named 'access_token'.
    """
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        user_email: str = payload.get("email")
        if user_id is None or user_email is None:
            raise credentials_exception
        return {"user_id": user_id, "user_email": user_email}
    except ExpiredSignatureError:
        traceback.print_exc()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Session expired. Please login again.")
    except JWTError:
        traceback.print_exc()
        raise credentials_exception
    except Exception:
        traceback.print_exc()
        raise HTTPException(status_code=401, detail="Not Authenticated")

def validate_user_request(access_token: str = Cookie(None)):
    # A thin wrapper or alias if you prefer a different name
    return get_current_user(access_token)

def log_user(user_id, user_email, user_name, user_pic, first_logged_in, last_accessed):
    """
    Ensure you have defined host, database, user, password somewhere or via env vars:
    e.g., DB_HOST, DB_NAME, DB_USER, DB_PASSWORD.
    """
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    try:
        connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        if connection.is_connected():
            cursor = connection.cursor()
            sql_query = """SELECT COUNT(*) FROM users WHERE email_id = %s"""
            cursor.execute(sql_query, (user_email,))
            row_count = cursor.fetchone()[0]
            if row_count == 0:
                sql_query = """
                    INSERT INTO users (user_id, email_id, user_name, user_pic, first_logged_in, last_accessed)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql_query, (user_id, user_email, user_name, user_pic, first_logged_in, last_accessed))
            else:
                # Optionally update last_accessed
                sql_query = """
                    UPDATE users SET last_accessed = %s WHERE email_id = %s
                """
                cursor.execute(sql_query, (last_accessed, user_email))
            connection.commit()
    except Error as e:
        logger.error("Error while connecting to MySQL in log_user: %s", e)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def log_token(access_token, user_email, session_id):
    host = os.getenv("DB_HOST")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    try:
        connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        if connection.is_connected():
            cursor = connection.cursor()
            sql_query = """INSERT INTO issued_tokens (token, email_id, session_id) VALUES (%s, %s, %s)"""
            cursor.execute(sql_query, (access_token, user_email, session_id))
            connection.commit()
    except Error as e:
        logger.error("Error while connecting to MySQL in log_token: %s", e)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            logger.info("MySQL connection is closed in log_token")

@router.get("/login")
async def login(request: Request):
    """
    Initiate Google OAuth2 login. Clears session, stores redirect target, and sends user to Google.
    """
    # Ensure SessionMiddleware is active in your main app.
    request.session.clear()

    # Where to redirect after login; e.g., your frontend app URL
    frontend_url = os.getenv("FRONTEND_URL")
    if not frontend_url:
        raise HTTPException(status_code=500, detail="FRONTEND_URL not configured")

    # Store where to go after auth
    request.session["login_redirect"] = frontend_url

    # Build redirect_uri for Google callback
    redirect_uri = os.getenv("REDIRECT_URL") 
    if not redirect_uri:
        raise HTTPException(status_code=500, detail="REDIRECT_URL not configured")

    # Redirect user to Google's OAuth consent page
    return await oauth.auth_demo.authorize_redirect(request, redirect_uri)

@router.get("/auth")  # use GET since Google does GET with code
async def auth(request: Request):
    """
    Callback endpoint for Google OAuth2.
    """
    try:
        # Exchange code for token
        token = await oauth.auth_demo.authorize_access_token(request)
        print(token) 
        # token is a dict containing access_token, id_token, expires_in, etc.
    except Exception as e:
        logger.error("Failed to obtain access token: %s", e, exc_info=True)
        raise HTTPException(status_code=401, detail="Token not received or invalid.")

    # Parse ID token to get claims
    try:
        user_claims = await oauth.auth_demo.parse_id_token(request, token)
    except Exception as e:
        # Fallback: call userinfo endpoint manually
        logger.warning("parse_id_token failed, falling back to userinfo endpoint: %s", e)
        try:
            resp = requests.get(
                "https://www.googleapis.com/oauth2/v2/userinfo",
                headers={"Authorization": f'Bearer {token["access_token"]}'}
            )
            resp.raise_for_status()
            user_claims = resp.json()
            print(f"\nuserinfo: {user_claims}")
        except Exception as e2:
            logger.error("Failed to fetch userinfo: %s", e2, exc_info=True)
            raise HTTPException(status_code=401, detail="Google authentication failed.")

    # Example of expected fields in user_claims: sub, email, name, picture, iss, exp, etc.
    user_id = user_claims.get("sub")
    user_email = user_claims.get("email")
    user_name = user_claims.get("name")
    user_pic = user_claims.get("picture")
    iss = user_claims.get("iss")
    # Basic checks
    if not user_id or not user_email:
        #raise HTTPException(status_code=401, detail="Google authentication failed: missing subject/email.")
        print("Google authentication failed: missing subject/email.")

    # Create our own JWT (cookie) for session
    expires_in = token.get("expires_in", 3600)
    access_token_expires = timedelta(seconds=expires_in)
    # Our payload includes sub and email
    our_token = create_access_token(data={"sub": user_id, "email": user_email}, expires_delta=access_token_expires)

    # Log user and token in DB
    session_id = str(uuid.uuid4())
    now = datetime.utcnow()
    try:
        log_user(user_id, user_email, user_name, user_pic, first_logged_in=now, last_accessed=now)
        log_token(our_token, user_email, session_id)
    except Exception:
        # Log but do not fail login for DB errors
        logger.exception("Error logging user/token to database")

    # Redirect back to frontend
    redirect_url = request.session.pop("login_redirect", None) or "/"
    response = RedirectResponse(url=redirect_url)
    # Set cookie named "access_token"
    response.set_cookie(
        key="access_token",
        value=our_token,
        httponly=True,       # better to use httponly=True for security
        secure=False,        # in production use True under HTTPS
        samesite="lax",      # adjust as needed
        max_age=expires_in,  # optional: set max_age so browser knows expiry
    )
    return response
