from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import auth, users
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (si luego quieres cerrar conexiones, logs, etc.)


app = FastAPI(
    title="User Management API",
    version="1.0.0",
    description="REST API with JWT authentication and user CRUD.",
    lifespan=lifespan,
)

app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(users.router, prefix="/api/v1", tags=["users"])


@app.get("/health", tags=["health"])
def health() -> dict:
    return {"status": "ok"}
