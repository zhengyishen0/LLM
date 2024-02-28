#!/usr/bin/env python3
# %%
from modules.openai_whisper import openai_whisper
import speech_recognition as sr


# obtain path to "english.wav" in the same folder as this script
AUDIO_FILE = "data/audio.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file


# %%

try:
    print(
        f"Whisper thinks you said {openai_whisper(audio)}")
except sr.RequestError as e:
    print("Could not request results from Whisper API")


# %%
