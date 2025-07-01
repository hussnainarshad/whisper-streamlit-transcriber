from openai import OpenAI
import tempfile
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()


def transcribe_audio(audio_file):
    transcription = client.audio.transcriptions.create(
        model="gpt-4o-transcribe", 
        file=audio_file  # already file-like
    )
    return transcription.text
