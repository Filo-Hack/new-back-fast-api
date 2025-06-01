from fastapi import FastAPI
from api import routes_upload, routes_gpt, routes_sensor, routes_dev

app = FastAPI(
    title="LLM Connector",
    description="Base project for text/audio input and LLM backend",
    version="0.1.0"
)

app.include_router(routes_upload.router, prefix="/upload", tags=["Upload"])
app.include_router(routes_gpt.router, prefix="/gpt", tags=["LLM"])
app.include_router(routes_sensor.router, prefix="/data", tags=["Sensor"])
app.include_router(routes_dev.router, prefix="/dev", tags=["Dev"])

