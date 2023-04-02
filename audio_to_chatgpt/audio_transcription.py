import whisper
from settings import WHISPER_MODEL, WHISPER_RESULT_TEXT_KEY


def transcribe(audio_file_path: str):
    model = whisper.load_model(WHISPER_MODEL)
    result = model.transcribe(audio_file_path, fp16=False)
    return result[WHISPER_RESULT_TEXT_KEY]
