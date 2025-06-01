# TTS/utils.py

from datetime import datetime, timedelta
from random import choice, choices
from typing import List, Dict

def generate_dummy_events(n: int = 100) -> List[Dict]:
    base_time = datetime(2025, 5, 31, 16, 0, 0)
    objects = [
        "стиральная машина", "настольная лампа", "штора", "кофемашина", "чайник",
        "входная дверь", "дверь в ванную", "дверь в гостиную"
    ]
    device_events = [
        "была включена", "была выключена", "была открыта", "была закрыта",
        "начала работу", "завершила цикл", "отправила уведомление"
    ]
    extra_facts = [
        "Я люблю принимать душ под музыку",
        "Я всегда пью чай перед сном",
        "Я не выхожу из дома без чашки кофе",
        "Я предпочитаю читать в тишине",
        "Я встаю каждый день в 6 утра",
        "Я не люблю яркий свет по вечерам",
        "Я слежу за температурой в комнате",
        "Я закрываю шторы, когда начинаю работать",
        "Я проверяю входную дверь перед сном",
        "Я включаю лампу при чтении"
    ]
    extra_requests = [
        "Как улучшить концентрацию?", "Как лучше высыпаться?",
        "Что делать, если нет мотивации?", "Что почитать вечером перед сном?",
        "Как избавиться от тревоги?", "Как сделать утро бодрым?"
    ]
    text_sources = {
        "fact": extra_facts,
        "request": extra_requests
    }

    entries = []
    for i in range(n):
        type_choice = choices(["fact", "request", "device"], weights=[0.4, 0.4, 0.2])[0]
        if type_choice == "device":
            obj = choice(objects)
            event = choice(device_events)
            text = f"В умном доме {obj} {event}"
        else:
            text = choice(text_sources[type_choice])
        timestamp = (base_time + timedelta(minutes=i * 3)).isoformat()
        entries.append({
            "text": text,
            "type_message": type_choice,
            "id": f"msg_{1000 + i}",
            "metadata": {
                "timestamp": timestamp
            }
        })
    return entries
