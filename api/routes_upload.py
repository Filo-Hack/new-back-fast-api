from fastapi import APIRouter, Form
from services.gpt_service import query_gpt
from models.response.upload import UploadResponse
from datetime import datetime
from uuid import uuid4
from TTS.ChatEngine import ChatEngine
from TTS.dbManager import ChromaDBManager

router = APIRouter()

# Новый способ инициализации ChatEngine
chroma_db = ChromaDBManager()
chat_engine = ChatEngine(chroma_db)

@router.post("/upload_speech", response_model=UploadResponse)
async def upload_text_audio(
    text: str = Form(...)
):
    message_id = f"msg_{uuid4().hex[:8]}"
    timestamp = datetime.now().isoformat()
    status = "device"

    record = [{
        "text": text,
        "timestamp": timestamp,
        "status": status
    }]

    # Сохраняем в БД
    chat_engine.save_record(record)

    # Генерируем промт из базы знаний
    prompt = chat_engine.generate_response(text)

    # Отправляем в LLM
    gpt_response = await query_gpt([{"role": "user", "content": prompt}])

    return UploadResponse(
        message="Файл получен",
        text=text,
        gpt_response=gpt_response
    )
