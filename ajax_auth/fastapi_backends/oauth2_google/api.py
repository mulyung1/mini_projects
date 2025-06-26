import os
from fastapi import FastAPI, Header, HTTPException, Depends, Request
from starlette.config import Config
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from apis import auth, chat
import time, requests

from dotenv import load_dotenv
load_dotenv(override=True)

config = Config(".env")

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=config("SECRET_KEY"))


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Add Session middleware

# # Logging time taken for each api request
@app.middleware("http")
async def log_response_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url.path} completed in {process_time:.4f} seconds")
    return response 

app.include_router(chat.router)
app.include_router(auth.router)

if __name__ == "__main__":
    import uvicorn
    import nest_asyncio
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=8000)
