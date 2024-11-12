import pathlib
import hashlib
from APIs import list_music, select_music, speech_to_text, image_search, download_image, reproduce_text

# Path template for saving downloaded images
TEMPLATE_IMAGE_SAVE_PATH = "images/downloaded_image.png"

class MusicApp:

    def __init__(self):
        """
        Initialize the MusicApp class.
        """
        # Set the current folder to the directory of this script
        self.current_folder = pathlib.Path(__file__).parent.resolve()
        # Initialize the extracted song filename
        self.extracted_song = ""

    def list_available_music(self) -> list[str]:
        """
        List available music using the list_music API.
        
        Returns:
            list[str]: A list of available song names.
        """
        return list_music.listAvailableMusic()
    
    def import_song(self, song_name: str) -> bool:
        """
        Import the song using the select_music API.
        
        Args:
            song_name (str): The name of the song to be imported.
        
        Returns:
            bool: True if the song was successfully imported, False otherwise.
        """
        ret_val = select_music.importSong(song_name)
        
        # Generate a unique filename based on the song name
        self.extracted_song = hashlib.md5(song_name.encode()).hexdigest()

        if ret_val != 1:
            # Save the imported song to the current folder with the generated filename
            with open(f"{self.current_folder.as_posix()}/{self.extracted_song}.mp3", "wb") as f:
                f.write(ret_val.content)
            return True
        return False
    
    def extract_text(self) -> str:
        """
        Extract text from the imported song.
        
        Returns:
            str: The extracted text (lyrics) from the song.
        """
        # Initialize the VoiceAI object
        vai = speech_to_text.initialize_voice_ai()
        # Create a transcription job for the imported song
        job_id = speech_to_text.create_transcription_job(vai, f"{self.current_folder.as_posix()}/{self.extracted_song}.mp3")
        # Poll until the transcription job is complete and get the result
        result = vai.poll_until_complete(job_id)
        # Extract and return the transcription words from the result
        return speech_to_text.extract_transcription_words(result)

    def search_and_download_image(self, text: str) -> str:
        """
        Search for an image based on the extracted text and download it.
        
        Args:
            text (str): The text to be used for the image search.
        
        Returns:
            str: The path to the downloaded image, or None if no image was found.
        """
        # Perform an image search using the image_search API
        image_url = image_search.perform_image_search(text)
        if image_url:
            # Define the path to save the downloaded image
            image_save_path = f"{self.current_folder.as_posix()}/{TEMPLATE_IMAGE_SAVE_PATH}"
            # Download the image using the download_image API
            download_image.download_image(image_url, image_save_path)
            return image_save_path
        return None

    def reproduce_text(self, text: str):
        """
        Reproduce the extracted text using text-to-speech.
        
        Args:
            text (str): The text to be converted to speech and played.
        """
        reproduce_text.reproduce_text(text)

    def clear_extracted_song(self):
        """
        Clear all downloaded songs in the folder and reset the list in the class.
        """
        # Check if the list of extracted songs is empty
        if self.extracted_song == "":
            return
              
        # Loop through all files in the current folder
        for element in self.current_folder.iterdir():
            # Check if the file is an MP3 file
            if element.is_file() and element.suffix == ".mp3":
                try:
                    # Remove the file
                    element.unlink()
                except OSError as e:
                    # Print an error message if the file removal fails
                    print(f"Failed to remove {element}: {e}")
        
        # Reset the extracted song filename
        self.extracted_song = ""