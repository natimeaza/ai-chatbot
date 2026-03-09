# app/api/routes/health.py
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Chatbot backend is running!"}