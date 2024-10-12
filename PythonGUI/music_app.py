import pathlib
from APIs import list_music, select_music, speech_to_text, image_search, download_image, reproduce_text

TEMPLATE_NAME = "song.mp3"
TEMPLATE_IMAGE_SAVE_PATH = "images/downloaded_image.png"

class MusicApp:
    def __init__(self):
        self.current_folder = pathlib.Path(__file__).parent.resolve().as_posix()

    def list_available_music(self):
        return list_music.listAvailableMusic()
    
    def import_song(self,song_name):
        ret_val = select_music.importSong(song_name)
        if ret_val != 1:
            with open(f"{self.current_folder}/{TEMPLATE_NAME}", "wb") as f:
                f.write(ret_val.content)
            return True
        return False
    
    def extract_text(self):
        vai = speech_to_text.initialize_voice_ai()
        job_id = speech_to_text.create_transcription_job(vai, f"{self.current_folder}/{TEMPLATE_NAME}")
        result = vai.poll_until_complete(job_id)
        return speech_to_text.extract_transcription_words(result)

    def search_and_download_image(self, text):
        image_url = image_search.perform_image_search(text)
        if image_url:
            image_save_path = f"{self.current_folder}/{TEMPLATE_IMAGE_SAVE_PATH}"
            download_image.download_image(image_url, image_save_path)
            return image_save_path
        return None

    def reproduce_text(self, text):
        reproduce_text.reproduce_text(text)