from FastAPI import FileResponse
from PythonGUI.APIs import speech_to_text

def extract_song(song: FileResponse, path: str):
    with open(f"{path}/song.mp3", "wb") as f:
        f.write(song)

def speech_to_text(path: str):
    vai = speech_to_text.initialize_voice_ai()
    job_id = speech_to_text.create_transcription_job(vai, f"{path}/song.mp3")
    result = vai.poll_until_complete(job_id)
    return speech_to_text.extract_transcription_words(result)

def download_image(image_url: str, path: str):
    image_save_path = f"{path}/images/downloaded_image.png"
    download_image.download_image(image_url, image_save_path)