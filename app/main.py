from fastapi import FastAPI
from app.api.routes import router as api_router
from app.config.db import global_init
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env.

app = FastAPI()

global_init()

app.include_router(api_router)
