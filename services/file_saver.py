import os
import shutil
from fastapi import UploadFile

TEMP_DIR = "tmp"

async def save_temp_audio(audio: UploadFile) -> str:
    os.makedirs(TEMP_DIR, exist_ok=True)
    file_path = os.path.join(TEMP_DIR, audio.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    return file_path
