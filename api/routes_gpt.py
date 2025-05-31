from fastapi import APIRouter
from models.request.gpt import ChatRequest
from models.response.gpt import ChatResponse
from services.gpt_service import query_gpt

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response_text = await query_gpt(request.chat_history, request.max_new_tokens)
    return ChatResponse(response=response_text)
