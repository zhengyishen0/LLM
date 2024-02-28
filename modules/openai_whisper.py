from openai import OpenAI


def transcription(audio=None, audio_file=None):
    client = OpenAI()

    audio = audio or open(audio_file, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio
    )
    return transcription.text
