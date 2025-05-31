from pydantic import BaseModel

class SensorDataResponse(BaseModel):
    message: str
    sensor_id: str
