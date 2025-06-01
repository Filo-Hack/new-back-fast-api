from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from services.file_saver import save_temp_audio
from services.transcriber import transcribe_audio
from services.gpt_service import query_gpt
from models.response.upload import UploadResponse
from TTS.chatEngine import ChatEngine
from TTS.dbManager import ChromaDBManager
import os
router = APIRouter()
chat_history = []

ALLOWED_EXTENSIONS = {".mp3", ".wav", ".m4a"}

# Инициализируем движки
db = ChromaDBManager()
chat_engine = ChatEngine(chroma_db=db)
 
@router.post("/upload_speech", response_model=UploadResponse)
async def upload_text_audio(audio: UploadFile = File(...)):
    ext = os.path.splitext(audio.filename)[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format: {ext}"
        )

    # 1. Сохраняем временно аудио
    path = await save_temp_audio(audio)

    print(path)

    # 2. Распознаём речь
    try:
        transcribed_text = transcribe_audio(path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Speech recognition failed: {e}")

    # 3. Сохраняем в ChromaDB
    try:
        chat_engine.save_record([{"text": transcribed_text}])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB save failed: {e}")

    # 4. Генерируем промт
    try:
        prompt = chat_engine.generate_response(transcribed_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prompt generation failed: {e}")

    # 5. Отправляем запрос в GPT
    chat_history.append({"role": "user", "content": prompt})
    try:
        gpt_response = await query_gpt(chat_history)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT query failed: {e}")
    chat_history.append({"role": "assistant", "content": gpt_response})

    # 6. Возвращаем клиенту
    return UploadResponse(
        message="Аудио успешно обработано",
        text=transcribed_text,
        audio_path=path,
        gpt_response=gpt_response
    )

