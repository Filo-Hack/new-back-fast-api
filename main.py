from fastapi import FastAPI
from api import routes_upload, routes_sensor

app = FastAPI(
    title="LLM Connector",
    description="Base project for text/audio input and LLM backend",
    version="0.1.0"
)

app.include_router(routes_upload.router, prefix="/upload_speech", tags=["Upload"])
app.include_router(routes_sensor.router, prefix="/data", tags=["SensorData"])