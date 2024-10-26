import os, sys
from fastapi.responses import FileResponse
import neuralspace as ns
from typing import Dict, Any

def extract_song(song: FileResponse, path: str):
    with open(f"{path}/song.mp3", "wb") as f:
        f.write(song.content)

def speech_to_text(path: str):
    vai = initialize_voice_ai()
    job_id = create_transcription_job(vai, f"{path}/song.mp3")
    result = vai.poll_until_complete(job_id)
    return extract_transcription_words(result)

def download_image(image_url: str, path: str):
    image_save_path = f"{path}/images/downloaded_image.png"
    download_image.download_image(image_url, image_save_path)

#-----------------------------------------------------------------------------------------------------------------------
# API key for STT
STT_API_KEY: str = "sk_a58a31d32bed7896a38ea55fa93fe8a1d709851e37e38c67e163c6004c9a0186"

# Initialize VoiceAI with API key
def initialize_voice_ai() -> ns.VoiceAI:
    return ns.VoiceAI(api_key=STT_API_KEY)

# Setup job configuration
def create_transcription_job(vai: ns.VoiceAI, filename: str) -> str:
    config= {
        'file_transcription': {
            'language_id': 'en',
            'mode': 'advanced',
        }
    }
    job_id = vai.transcribe(file=filename, config=config)
    print(f'Created job: {job_id}')
    return job_id

# Extract words from transcription result
def extract_transcription_words(result: Dict[str, Any]) -> str:
    timestamps = result['data']['result']['transcription']['channels']['0']['timestamps']
    print(result)
    words = [entry['word'] for entry in timestamps]
    return " ".join(words)