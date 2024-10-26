import sys
import os
from API_Output_Manipulation import functions
from fastapi.responses import FileResponse
import pathlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../PythonGUI")))
from APIs import download_image, image_search, list_music, select_music

# You have available the following functions
# ----------------------------------------------------------------------------------------------------------------------------------------------
# download_image.download_image()           Given as input the url of the string and where to save it, downloads an image from the internet
# image_search.perform_image_search()       Given a string with the content to search on the internet, returns the url of an image found
# list_music.listAvailableMusic()           Returns a list with all the names of the song available for import (strings)
# select_music.importSong()                 Given a string with the name of the song, returns a FileResponse that contains a file with that song

# functions.download_image()                Given an image url and a path, download that image in the specified path
# functions.extract_song()                  Given a FileResponse and a path, downloads the song in the specified path
# functions.speech_to_text()                Given the path to a song, extracts its lyrics
# ----------------------------------------------------------------------------------------------------------------------------------------------

# And the following constants which are used to specify the paths of songs and images
SONG_PATH = pathlib.Path(__file__).parent.resolve().as_posix()
IMAGE_PATH = SONG_PATH + "/images/downloaded_image.png"

# Write a main function that performs the following composition:
# List songs -> Import 1st song available -> Extract lyrics from that song -> Perform a google search using the lyrics ->
# Use the link returned from the image search to download that image

def main():

    # SOLUTION
    song_list = list_music.listAvailableMusic()
    print(song_list)
    selected_song: FileResponse = select_music.importSong(song_list[0])
    functions.extract_song(selected_song, SONG_PATH)
    song_text = functions.speech_to_text(SONG_PATH)
    print(song_text)
    url = image_search.perform_image_search(song_text)
    print(url)
    download_image.download_image(url,IMAGE_PATH)
    print("finito, so nice!")

    # WRITE HERE
   


if __name__ == "__main__":
    main()