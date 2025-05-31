from pydantic import BaseModel
from datetime import datetime

class SensorDataRequest(BaseModel):
    sensor_id: str
    status: str  # можно заменить на bool, если статус только True/False
    timestamp: datetime
