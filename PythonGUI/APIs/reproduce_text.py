import pathlib
from gtts import gTTS
import pygame
import time

def reproduce_text(input_text: str):
    """
    This function is used to reproduce the transcribed text.
    Leveraging the Google Text-To-Speech API wrapped by the library gtts,
    and Pygame to reproduce the audio.
    
    Args:
        input_text (str): The text to be converted to speech and played.
    """
    # Set the language for the text-to-speech conversion
    language = 'en'
    
    # Create a gTTS object with the input text and specified language
    myobj = gTTS(text=input_text, lang=language, slow=False)
    
    # Get the current folder path
    current_folder = pathlib.Path(__file__).parent.resolve().as_posix()
    
    print("Creating audio from text...")
    
    # Save the generated speech to an MP3 file in the current folder
    myobj.save(current_folder + "/tts.mp3")
    
    # Initialize the pygame mixer
    pygame.mixer.pre_init()
    pygame.mixer.init()
    
    # Load the MP3 file into the pygame mixer
    pygame.mixer.music.load(current_folder + "/tts.mp3")
    
    # Delay needed to fully load the audio
    time.sleep(5)
    
    # Play the loaded MP3 file
    pygame.mixer.music.play()