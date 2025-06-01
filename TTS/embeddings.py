from langchain_community.embeddings import HuggingFaceEmbeddings
from TTS.config import settings

embeddings = HuggingFaceEmbeddings(
    model_name=settings.LM_MODEL_NAME,
    model_kwargs={"device": "cuda"}  # или "cuda" если у тебя есть GPU
)