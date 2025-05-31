from fastapi import APIRouter, File, Form, UploadFile
from services.file_saver import save_temp_audio
from models.response.upload import UploadResponse

router = APIRouter()

@router.post("/", response_model=UploadResponse)
async def upload_text_audio(
    text: str = Form(...),
    audio: UploadFile = File(...)
):
    path = await save_temp_audio(audio)
    return UploadResponse(message="Файл получен", text=text, audio_path=path)
