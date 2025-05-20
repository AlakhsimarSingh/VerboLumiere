import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from .audio_utils import load_audio_for_whisper

processor = WhisperProcessor.from_pretrained("openai/whisper-large")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")

def transcribe_audio(audio_path, target_lang="en"):
    waveform = load_audio_for_whisper(audio_path)
    inputs = processor(waveform, sampling_rate=16000, return_tensors="pt", padding=True)
    input_features = inputs.input_features
    attention_mask = inputs.attention_mask if 'attention_mask' in inputs else None

    with torch.no_grad():
        predicted_ids = model.generate(input_features, language=target_lang, attention_mask=attention_mask)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription