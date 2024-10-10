import pathlib
from gtts import gTTS
import pygame
import time

def reproduce_text(input_text):
    language = 'en'
    myobj = gTTS(text=input_text, lang=language, slow=False)
    current_folder = pathlib.Path(__file__).parent.resolve().as_posix()
    print("Creating audio from text...")
    myobj.save(current_folder+"/tts.mp3")
    pygame.mixer.pre_init()
    pygame.mixer.init()
    pygame.mixer.music.load(current_folder+"/tts.mp3")
    time.sleep(5) # Delay needed to fully load the audio
    pygame.mixer.music.play()