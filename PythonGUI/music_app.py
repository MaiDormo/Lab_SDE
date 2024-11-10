import pathlib
import hashlib
from APIs import list_music, select_music, speech_to_text, image_search, download_image, reproduce_text

TEMPLATE_IMAGE_SAVE_PATH = "images/downloaded_image.png"

class MusicApp:

    def __init__(self):
        self.current_folder = pathlib.Path(__file__).parent.resolve()
        self.extracted_song = ""

    def list_available_music(self):
        return list_music.listAvailableMusic()
    
    def import_song(self, song_name):
        ret_val = select_music.importSong(song_name)
        
        # Generate a unique filename based on the song name
        self.extracted_song = hashlib.md5(song_name.encode()).hexdigest()

        if ret_val != 1:
            with open(f"{self.current_folder.as_posix()}/{self.extracted_song}.mp3", "wb") as f:
                f.write(ret_val.content)
            return True
        return False
    
    def extract_text(self):
        vai = speech_to_text.initialize_voice_ai()
        job_id = speech_to_text.create_transcription_job(vai, f"{self.current_folder.as_posix()}/{self.extracted_song}.mp3")
        result = vai.poll_until_complete(job_id)
        return speech_to_text.extract_transcription_words(result)

    def search_and_download_image(self, text):
        image_url = image_search.perform_image_search(text)
        if image_url:
            image_save_path = f"{self.current_folder.as_posix()}/{TEMPLATE_IMAGE_SAVE_PATH}"
            download_image.download_image(image_url, image_save_path)
            return image_save_path
        return None

    def reproduce_text(self, text):
        reproduce_text.reproduce_text(text)

    def clear_extracted_song(self):
        """Clear all downloaded songs in a folder and reset the list in the class.
            Note a song need to be imported in order to call this song"""
        
        # Check if the list of extracted songs is empty
        if self.extracted_song == "":
            return
              
        # Original loop with additional debugging
        for element in self.current_folder.iterdir():
            if element.is_file() and element.suffix == ".mp3":
                try:
                    element.unlink()
                except OSError as e:
                    print(f"Failed to remove {element}: {e}")
        
        # Reset the string value
        self.extracted_song = ""
