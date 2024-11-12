import os, sys
from fastapi.responses import FileResponse, Response
import neuralspace as ns
from typing import Dict, Any
import hashlib

# Add the PythonGUI directory to the system path for module imports
sys.path.append('./PythonGUI')
from APIs import select_music

def extract_song(song: FileResponse, path: str) -> str:
    """
    This function takes the MP3 song and rewrites it inside a specific folder,
    and returns the generated name (it's implemented as a hash of the song content).
    
    Args:
        song (FileResponse): The response containing the MP3 song file.
        path (str): The directory path where the song will be saved.
    
    Returns:
        str: The generated filename based on the hash of the song content.
    """
    # Generate a unique filename based on the content of the song
    filename = hashlib.md5(song.content).hexdigest()
    
    # Write the song content to a file in the specified path
    with open(f"{path}/{filename}.mp3", "wb") as f:
        f.write(song.content)
    
    return filename

def speech_to_text(path: str, filename: str) -> str:
    """
    This function takes the path (used to store the MP3 song before),
    and calls all of the functions related to Speech To Text.
    
    Args:
        path (str): The directory path where the song is saved.
        filename (str): The name of the song file.
    
    Returns:
        str: The extracted text (lyrics) from the song.
    """
    # Initialize the VoiceAI object
    vai = initialize_voice_ai()
    
    # Create a transcription job for the song file
    job_id = create_transcription_job(vai, f"{path}/{filename}.mp3")
    
    # Wait for the transcription job to complete and get the result
    result = vai.poll_until_complete(job_id)
    
    # Extract and return the transcription words from the result
    return extract_transcription_words(result)

def download_image(image_url: str, path: str):
    """
    This is a wrapper function: given a URL and a path, it is used to download the image inside the "images" folder.
    If the folder is not present, it will create it.
    
    Args:
        image_url (str): The URL of the image to be downloaded.
        path (str): The directory path where the image will be saved.
    """
    # Define the path to save the downloaded image
    image_save_path = f"{path}/images/downloaded_image.png"
    
    # Download the image using the download_image API
    download_image.download_image(image_url, image_save_path)

# API key for Speech-To-Text (STT) service
STT_API_KEY: str = "sk_a58a31d32bed7896a38ea55fa93fe8a1d709851e37e38c67e163c6004c9a0186"

def initialize_voice_ai() -> ns.VoiceAI:
    """
    Initialize VoiceAI with API key.

    Returns:
        ns.VoiceAI: The initialized VoiceAI object.
    """
    return ns.VoiceAI(api_key=STT_API_KEY)

def create_transcription_job(vai: ns.VoiceAI, filename: str) -> str:
    """
    Setup job configuration and create a transcription job.
    
    Args:
        vai (ns.VoiceAI): The initialized VoiceAI object.
        filename (str): The name of the song file.
    
    Returns:
        str: The job ID of the created transcription job.
    """
    # Configuration for the transcription job
    config = {
        'file_transcription': {
            'language_id': 'en',  # Set the language to English
            'mode': 'advanced',   # Set the mode to advanced
        }
    }
    
    # Create a transcription job with the specified file and configuration
    job_id = vai.transcribe(file=filename, config=config)
    print(f'[CREATED JOB]: {job_id}')
    
    return job_id

def extract_transcription_words(result: Dict[str, Any]) -> str:
    """
    Extract words from transcription result.
    
    Args:
        result (Dict[str, Any]): The result of the transcription job.
    
    Returns:
        str: The extracted words concatenated with a single space (" ").
    """
    # Extract all timestamps from the transcription result
    timestamps = result['data']['result']['transcription']['channels']['0']['timestamps']
    print(f"[STT RESULT]: {result}")
    
    # Gather all words from the timestamps
    words = [entry['word'] for entry in timestamps]
    
    # Return all words concatenated with a single space (" ")
    return " ".join(words)