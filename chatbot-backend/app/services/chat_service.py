import os
import httpx
from typing import Optional

# For now, using OpenAI as example
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def generate_response(message: str) -> str:
    """
    Generate a response using OpenAI API.
    """
    if not message.strip():
        return "Please provide a message."

    if not OPENAI_API_KEY:
        return "AI service not configured. Please set OPENAI_API_KEY."

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [{"role": "user", "content": message}],
                    "max_tokens": 150,
                },
                timeout=10.0,
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating response: {str(e)}"