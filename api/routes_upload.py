# from fastapi import APIRouter, File, Form, UploadFile, HTTPException
# from services.file_saver import save_temp_audio
# from services.gpt_service import query_gpt
# from models.response.upload import UploadResponse
# import os

# router = APIRouter()
# chat_history = []

# ALLOWED_EXTENSIONS = {".mp3", ".wav", ".m4a"}

# @router.post("/upload_speech", response_model=UploadResponse)
# async def upload_text_audio(
#     text: str = Form(...),
#     audio: UploadFile = File(...)
# ):
#     print(text)
#     # Проверка расширения файла
#     ext = os.path.splitext(audio.filename)[-1].lower()
#     if ext not in ALLOWED_EXTENSIONS:
#         raise HTTPException(
#             status_code=400,
#             detail=f"Неподдерживаемый формат файла: {ext}. Допустимые форматы: {', '.join(ALLOWED_EXTENSIONS)}"
#         )

#     path = await save_temp_audio(audio)

#     # Формируем чат для запроса к LLM
#     chat_history.append({"role": "user", "content": text})
#     llm_response = await query_gpt(chat_history)
#     chat_history.append({"role": "assistant", "content": llm_response})
    
#     return UploadResponse(
#         message="Файл получен",
#         text=text,
#         audio_path=path,
#         gpt_response=llm_response
#     )