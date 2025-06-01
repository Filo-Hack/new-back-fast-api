import os
import shutil
from fastapi import UploadFile

TEMP_DIR = "tmp"
TARGET_FILENAME = "audio.wav"

async def save_temp_audio(audio: UploadFile) -> str:
    os.makedirs(TEMP_DIR, exist_ok=True)
    file_path = os.path.join(TEMP_DIR, TARGET_FILENAME)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    return file_path
