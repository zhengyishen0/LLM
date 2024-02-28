from modules.gcp_storage import upload_blob
import replicate
import time
import os


def fast_whisper(audio_uri=None, audio_file=None):

    start_time = time.time()

    uri = audio_uri or upload_blob(audio_file)

    output = replicate.run(
        "vaibhavs10/incredibly-fast-whisper:3ab86df6c8f54c11309d4d1f930ac292bad43ace52d10c80d87eb258b3c9f79c",
        input={
            "task": "transcribe",
            "audio": uri,
            "language": "None",
            "timestamp": "chunk",
            "batch_size": 64,
            "diarise_audio": False,
            "hf_token": os.environ.get("HF_TOKEN"),
        }
    )
    print(f"{time.time() - start_time} seconds")
    print(output)
