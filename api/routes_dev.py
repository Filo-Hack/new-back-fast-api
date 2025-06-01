from fastapi import APIRouter
from TTS.ChatEngine import ChatEngine
from TTS.dbManager import ChromaDBManager
from datetime import datetime, timedelta
import random

router = APIRouter()
chroma_db = ChromaDBManager()
chat_engine = ChatEngine(chroma_db=chroma_db)


@router.post("/fill_vector_db")
async def fill_vector_db():
    base_time = datetime(2025, 5, 31, 16, 0, 0)

    objects = [
        "стиральная машина", "настольная лампа", "штора", "кофемашина", "чайник",
        "входная дверь", "дверь в ванную", "дверь в гостиную"
    ]

    device_events = [
        "была включена", "была выключена", "была открыта", "была закрыта",
        "начала работу", "завершила цикл", "отправила уведомление"
    ]

    user_requests = [
        "Как улучшить концентрацию?",
        "Что почитать вечером?",
        "Дай советы перед экзаменом",
        "Как стать продуктивнее?",
        "Я люблю вайбкодить, как поддерживать настрой?",
        "Как высыпаться, если сплю 6 часов?",
        "Как улучшить качество сна матери?",
        "Я люблю душнить, чем это плохо?",
        "Как выйти из депрессии?",
        "Что поможет мне почувствовать себя лучше?",
        "Как поднять настроение другу?",
        "Я люблю пить кофе. Это вредно?",
        "Я принимаю душ в 7 вечера. Это нормально?",
        "Что почитать перед сном?",
        "Я люблю пить пиво, но за ЗОЖ — что делать?",
    ]

    entries = []
    for i in range(100):
        choice = random.choice(["device", "request"])
        timestamp = (base_time + timedelta(minutes=i * 3)).isoformat()

        if choice == "device":
            obj = random.choice(objects)
            event = random.choice(device_events)
            text = f"В умном доме {obj} {event}"
        else:
            text = random.choice(user_requests)

        entries.append({
            "text": text,
            "status": choice,
            "timestamp": timestamp
        })

    # Сохраняем векторные записи
    chat_engine.save_record(entries)

    return {"message": f"Добавлено {len(entries)} записей в ChromaDB"}
