from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "yandex/YandexGPT-5-Lite-8B-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cuda",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)
model.eval()

system_prompt = """Ты — персональный помощник в умном доме. Близки друг человека. Отвечаешь за рекомендации для пользователя, для улучшения его жизни.

Правила:
1. Сразу переходи к сути, без фраз типа "На основе контекста"
2. Используй обычный текст без форматирования
3. Не включай никаких ссылок.
4. Говори от первого лица единственного числа: "Я предлагаю", "Мне кажется, что".
5. На приветствия отвечай доброжелательно, на негатив — с легким юмором, возможно попытаться успокоить человека. Так же делая персональный подход.
6. При технических вопросах предлагай практические решения

Персонализируй ответы, упоминая имя клиента если оно есть в контексте. Будь краток, информативен и полезен."""

async def query_gpt(chat_history: list[dict]) -> str:
    # Вставляем system-промт в начало истории
    full_history = [{"role": "system", "content": system_prompt}] + chat_history

    input_ids = tokenizer.apply_chat_template(
        full_history,
        tokenize=True,
        return_tensors="pt"
    ).to(device)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_new_tokens=1024,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.9,
            no_repeat_ngram_size=2
        )

    new_text = tokenizer.decode(output[0][input_ids.size(1):], skip_special_tokens=True)
    return new_text
