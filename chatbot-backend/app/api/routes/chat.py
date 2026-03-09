from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):
    ai_response = await generate_response(request.message)

    return {
        "response": ai_response
    }