from API_Output_Manipulation import functions
from PythonGUI.APIs import download_image, image_search, list_music, select_music
import pathlib

# You have available the following functions
# ----------------------------------------------------------------------------------------------------------------------------------------------
# download_image.download_image()           Given as input the url of the string and where to save it, downloads an image from the internet
# image_search.perform_image_search()       Given a string with the content to search on the internet, returns the url of an image found
# list_music.listAvailableMusic()           Returns a list with all the names of the song available for import (strings)
# select_music.importSong()                 Given a string with the name of the song, returns a FileResponse that contains a file with that song

# functions.download_image()                Given an image url and a path, download that image in the specified path
# functions.extract_song()                  Given a FileResponse and a path, downloads the image in the specified path
# functions.speech_to_text()                Given the path to a song, extracts its lyrics
# ----------------------------------------------------------------------------------------------------------------------------------------------

# And the following constants which are used to specify the paths of songs and images
CURRENT_PATH = pathlib.Path(__file__).parent.resolve().as_posix()
SONG_PATH = CURRENT_PATH+"/song.mp3"
IMAGE_PATH = CURRENT_PATH+"/images/downloaded_image.png"

# Write a main function that performs the following composition:
# List songs -> Import 1st song available -> Extract lyrics from that song -> Perform a google search using the lyrics ->
# Use the link returned from the image search to download that image

def main():

    # WRITE HERE

    return 0