from pydantic import BaseModel

class UploadResponse(BaseModel):
    message: str
    text: str
    audio_path: str
