from pydantic import BaseModel
from typing import List, Dict

class ChatRequest(BaseModel):
    chat_history: List[Dict]
    max_new_tokens: int = 1024
