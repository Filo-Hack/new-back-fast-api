from fastapi import APIRouter
from models.request.sensor import SensorDataRequest
from models.response.sensor import SensorDataResponse

router = APIRouter()

@router.post("/sensor", response_model=SensorDataResponse)
async def receive_sensor_data(data: SensorDataRequest):
    # Тут ты можешь сохранять данные в БД или логировать
    print(f"Получены данные от датчика: {data.sensor_id}, статус: {data.status}, время: {data.timestamp}")

    return SensorDataResponse(
        message="Данные от датчика получены",
        sensor_id=data.sensor_id
    )
