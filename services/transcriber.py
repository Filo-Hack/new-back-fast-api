import whisper


def transcribe_audio(file_path: str) -> str:
    model = whisper.load_model("base")  # можно заменить на small, medium, large
    print(file_path)
    result = model.transcribe(file_path)
    print(result)
    return result["text"]
