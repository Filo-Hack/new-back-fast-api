from fastapi import APIRouter, File, Form, UploadFile
from services.file_saver import save_temp_audio
from services.gpt_service import query_gpt
from models.response.upload import UploadResponse

router = APIRouter()

@router.post("/upload_speech", response_model=UploadResponse)
async def upload_text_audio(
    text: str = Form(...),
    audio: UploadFile = File(...)
):
    path = await save_temp_audio(audio)

    # Формируем чат для запроса к LLM
    chat_history = [{"role": "user", "content": text}]
    llm_response = await query_gpt(chat_history)

    return UploadResponse(
        message="Файл получен",
        text=text,
        audio_path=path,
        gpt_response=llm_response
    )
