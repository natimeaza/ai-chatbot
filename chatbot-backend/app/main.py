# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import health, chat

from app.core.config import get_settings
# We'll import routers later

settings = get_settings()

app = FastAPI(
    title="AI Chatbot Backend",
    description="Backend for React + Python AI Chatbot project",
    version="0.1.0",
    docs_url="/docs",           # Swagger UI
    redoc_url="/redoc",
)
app.include_router(health, prefix="/api")
app.include_router(chat, prefix="/api")

# Allow React frontend (update origins later for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # your React port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "environment": "dev"}


# Later we will include api routers here like:
# app.include_router(api_router, prefix="/api/v1")