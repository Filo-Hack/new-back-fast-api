from fastapi import FastAPI
from api import upload_speech, routes_gpt, routes_sensor

app = FastAPI(
    title="LLM Connector",
    description="Base project for text/audio input and LLM backend",
    version="0.1.0"
)

app.include_router(upload_speech.router, prefix="/upload", tags=["Upload"])
app.include_router(routes_gpt.router, prefix="/gpt", tags=["LLM"])
app.include_router(routes_sensor.router, prefix="/data", tags=["Sensor"])
