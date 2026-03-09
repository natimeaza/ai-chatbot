from fastapi import FastAPI
from pydantic import BaseModel
from app.routes.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "AI Chatbot API running"}

@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message

    response = f"You asked: {user_message}"

    return {
        "response": response
    }