import numpy as np
from pydub import AudioSegment
import pyttsx3


def load_audio_for_whisper(audio_path, target_sample_rate=16000):
    audio = AudioSegment.from_file(audio_path).set_channels(1).set_frame_rate(target_sample_rate)
    samples = np.array(audio.get_array_of_samples()).astype(np.float32) / 32768.0  # normalize to [-1, 1]
    return samples

def text_to_speech(text, output_audio_path="media/translated_audio.mp3", language_code="en-US"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")
    for voice in voices:
        if language_code in voice.id:
            engine.setProperty("voice", voice.id)
            break
    engine.save_to_file(text, output_audio_path)
    engine.runAndWait()
    return output_audio_path