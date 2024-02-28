from __future__ import annotations

import os
from io import BytesIO

from speech_recognition.audio import AudioData
from speech_recognition.exceptions import SetupError


def openai_whisper(
    audio_data: "AudioData",
    *,
    model: str = "whisper-1",
    api_key: str | None = None,
):
    """
    Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the OpenAI Whisper API.

    This function requires an OpenAI account; visit https://platform.openai.com/signup, then generate API Key in `User settings <https://platform.openai.com/account/api-keys>`__.

    Detail: https://platform.openai.com/docs/guides/speech-to-text

    Raises a ``speech_recognition.exceptions.SetupError`` exception if there are any issues with the openai installation, or the environment variable is missing.
    """
    if not isinstance(audio_data, AudioData):
        raise ValueError("``audio_data`` must be an ``AudioData`` instance")
    if api_key is None and os.environ.get("OPENAI_API_KEY") is None:
        raise SetupError("Set environment variable ``OPENAI_API_KEY``")

    try:
        from openai import OpenAI
    except ImportError:
        raise SetupError(
            "missing openai module: ensure that openai is set up correctly."
        )
    client = OpenAI()

    wav_data = BytesIO(audio_data.get_wav_data())
    wav_data.name = "SpeechRecognition_audio.wav"

    transcript = client.audio.transcriptions.create(
        model=model,
        file=wav_data
    )
    return transcript.text


# def openai_whisper(audio=None, audio_file=None):
#     client = OpenAI()

#     audio = audio or open(audio_file, "rb")
#     transcription = client.audio.transcriptions.create(
#         model="whisper-1",
#         file=audio
#     )
#     return transcription.text
