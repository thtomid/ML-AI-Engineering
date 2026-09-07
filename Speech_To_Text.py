from django.templatetags.i18n import language
from transformers import pipeline
from kokoro import Kokoro
import torch

pipe = pipeline(
    "automatic-speech-recognition",
    model="vhdm/whisper-large-fa-v1",
    # device=0,               # GPU 0
    dtype=torch.float16
)

result = pipe(
    "Sound.m4a",
    chunk_length_s=30,
    batch_size=8
)

print(result["text"])