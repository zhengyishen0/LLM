import librosa
import soundfile as sf


def stretch(input, output, rate):
    y, sr = librosa.load(input)
    y_stretched = librosa.effects.time_stretch(y, rate=rate)
    duration = len(y_stretched) / sr
    sf.write(output, y_stretched, sr)
    print(f"Stretched audio to {duration} seconds")
    return y_stretched
