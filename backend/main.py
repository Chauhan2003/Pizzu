import os
from fastapi import FastAPI
from dotenv import load_dotenv

from routes.auth import auth_router
from routes.order import order_router

load_dotenv()

API_PREFIX = os.getenv("API_PREFIX", "/api/v1")  # fallback if not found

app = FastAPI()

app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(order_router, prefix=API_PREFIX)


@app.get("/health")
def check_health():
    return {
        "success": True,
        "message": "Server is healthy"
    }