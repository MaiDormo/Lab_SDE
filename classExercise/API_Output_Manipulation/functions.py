import os, sys
from fastapi.responses import FileResponse, Response
import neuralspace as ns
from typing import Dict, Any
sys.path.append('./PythonGUI')
from APIs import select_music
import hashlib



def extract_song(song: FileResponse, path: str) -> str:
    """This function takes the MP3 song and rewrites it inside a specific folder,
        returns the generated name (it's implemented as a hash of the song)"""
    
    filename = hashlib.md5(song.content).hexdigest()
    with open(f"{path}/{filename}.mp3", "wb") as f:
        f.write(song.content)
    return filename


def speech_to_text(path: str, filename: str) -> str:
    """This function takes the path (used to store the mp3 song before),
    and calls all of the function related to Speech To Text """
    vai = initialize_voice_ai()
    job_id = create_transcription_job(vai, f"{path}/{filename}.mp3")
    result = vai.poll_until_complete(job_id)
    return extract_transcription_words(result)


def download_image(image_url: str, path: str):
    """This function, given a url and a path, is used to download the image inside the "images" folder,
    if the folder is not present it will create it."""
    image_save_path = f"{path}/images/downloaded_image.png"
    download_image.download_image(image_url, image_save_path)

#-----------------------------------------------------------------------------------------------------------------------
# API key for STT
STT_API_KEY: str = "sk_a58a31d32bed7896a38ea55fa93fe8a1d709851e37e38c67e163c6004c9a0186"

 
def initialize_voice_ai() -> ns.VoiceAI:
    """Initialize VoiceAI with API key"""
    return ns.VoiceAI(api_key=STT_API_KEY)

def create_transcription_job(vai: ns.VoiceAI, filename: str) -> str:
    """Setup job configuration"""
    config= {
        'file_transcription': {
            'language_id': 'en',
            'mode': 'advanced',
        }
    }
    job_id = vai.transcribe(file=filename, config=config)
    print(f'Created job: {job_id}')
    return job_id

def extract_transcription_words(result: Dict[str, Any]) -> str:
    """Extract words from transcription result"""
    timestamps = result['data']['result']['transcription']['channels']['0']['timestamps']
    print(result)
    words = [entry['word'] for entry in timestamps]
    return " ".join(words)