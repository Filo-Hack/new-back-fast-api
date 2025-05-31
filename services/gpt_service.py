from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "yandex/YandexGPT-5-Lite-8B-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cuda" if device == "cuda" else "auto",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)
model.eval()

async def query_gpt(chat_history: list[dict], max_new_tokens: int = 1024) -> str:
    input_ids = tokenizer.apply_chat_template(
        chat_history,
        tokenize=True,
        return_tensors="pt"
    ).to(device)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.9,
            no_repeat_ngram_size=2
        )

    new_text = tokenizer.decode(output[0][input_ids.size(1):], skip_special_tokens=True)
    return new_text
