# Speech To Text

Voice is the most natural way for humans to communicate and it is my dream to build a voice-based AI that can be a always-there human companion. There I started the [Project H.E.R](project_her.md) -- a tribute to the movie ["her"](<https://en.wikipedia.org/wiki/Her_(film)>).

The first step to building such a system is to convert voice to text.

OpenAI's Whisper is a less known AI solution that is shadowed by the more popular ChatGPT, but it is a very powerful speech-to-text service.

## Whisper (OpenAI)

Using Whisper is very simple. We can use the `openai` python package or a simple http request to convert voice to text. The API takes a file as input and returns the transcribed text.

```python
from openai import OpenAI

client = OpenAI()

with open("audio.wav", "rb") as f:
    audio_file = f.read()

transcript = client.audio.transcriptions.create(
    model=model,
    file=audio_file  # load the audio file, not the path
)

print(transcript.text)
```

## Incredibly Fast Whisper

Whisper is great for short conversations, but when it comes to long audio files, it is not the best. An open-source project called [Incredibly Fast Whisper](https://github.com/Vaibhavs10/insanely-fast-whisper) can convert a 250 minutes audio file in just 100 seconds.

Using this package is insanely simple. Here's how to use it in CLI and Python.

```bash
pipx install insanely-fast-whisper

insanely-fast-whisper --file-name <filename or URL>
```

```python

import torch
from transformers import pipeline
from transformers.utils import is_flash_attn_2_available

pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v3", # select checkpoint from https://huggingface.co/openai/whisper-large-v3#model-details
    torch_dtype=torch.float16,
    device="cuda:0", # or mps for Mac devices
    model_kwargs={"attn_implementation": "flash_attention_2"} if is_flash_attn_2_available() else {"attn_implementation": "sdpa"},
)

outputs = pipe(
    "<FILE_NAME>",
    chunk_length_s=30,
    batch_size=24,
    return_timestamps=True,
)

outputs
```

### Replicate

What's even better is now you can use it without a local GPU.

You can just use the deployed service on [Replicate](https://replicate.com/vaibhavs10/incredibly-fast-whisper).
I've tested this API, the speed is as fast as Colab's T4 GPU.

## Real-Time Audio Streaming

The most important feature in building an always-there AI companion is real-time audio streaming. Thought Whisper is fast already, but it still takes 3-4 seconds to transcribe a minute-long audio. In our case, we need to transcribe the audio into a text, send text with the prompt to get a response, then convert the text response into an audio. That will take 10+ seconds to go through the entire process. In a real-world conversation scenario, it is not acceptable.

So one of the key task is to build a real-time transcriptions system.

The idea is simple, instead of waiting for the audio to finish and then send the file to the API, we can send the audio in chunks. But most chunking strategies are time-based, which means the system might cut off the audio in the middle of a word. That will make the quality of the transcription unpredictable.

As I was searching for a solution that can detect the volume of the audio and can chunk the audio when the people pause, I found a project called [Speech Recognition](https://github.com/Uberi/speech_recognition) that can not only chunk the audio but also transcribe it in several STT services like OpenAI, Google, Azure, etc.

While OpenAI's Whisper only takes a file as input, Google's [Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/docs/transcribe-streaming-audio) can take a stream as input. So we can use the Speech Recognition package to chunk the audio and send the chunks to Google's STT service.
