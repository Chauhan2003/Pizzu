from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.config import API_PREFIX
from core.database import connect_db
from routes.auth import auth_router
from routes.order import order_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    connect_db()
    print("Application started successfully.")

    yield

    # Shutdown
    print("Application shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(order_router, prefix=API_PREFIX)