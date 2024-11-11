from API_Output_Manipulation import functions
from fastapi.responses import FileResponse
import pathlib
import sys

sys.path.append('./PythonGUI')
from APIs import download_image, image_search, list_music, select_music

# You have available the following functions
# ----------------------------------------------------------------------------------------------------------------------------------------------
# download_image.download_image()           Given as input the url of the string and where to save it, downloads an image from the internet
# image_search.perform_image_search()       Given a string with the content to search on the internet, returns the url of an image found
# list_music.listAvailableMusic()           Returns a list with all the names of the song available for import (strings)
# select_music.importSong()                 Given a string with the name of the song, returns a FileResponse that contains a file with that song

# functions.download_image()                Given an image url and a path, download that image in the specified path
# functions.extract_song()                  Given a FileResponse and a path, downloads the song in the specified path
# functions.speech_to_text()                Given the path to a song and the generated name for the extracted song, extracts its lyrics
# ----------------------------------------------------------------------------------------------------------------------------------------------

# And the following constants which are used to specify the paths of songs and images
SONG_PATH = pathlib.Path(__file__).parent.resolve().as_posix() # Represent the folder location to which the song will be exported to.
IMAGE_PATH = SONG_PATH + "/images/downloaded_image.png" # Represent the template path were the image will be downloaded



"""
In LAB Exercise:
    - you need to add the underlined two lines of code in order to make the whole main function work,
    thus completing all of the APIs calls shown before.
"""
def main():
    song_list = list_music.listAvailableMusic() #this function can be found inside PythonGUI/APIs/list_music.py
    print(song_list)

    selected_song = select_music.importSong(song_list[0]) #this function can be found inside PythonGUI/APIs/select_music.py

    # Insert a call to the function extract_song() which can be found inside the functions.py file
    # It takes as input a song: FileResponse and the SONG_PATH, and returns a filename
    # ----------------------------------------- WRITE HERE --------------------------------------------------

    # Insert a call to the function speech_to_text() which can be found inside the API_Output_Manipulation/functions.py file
    # It takes as input a SONG_PATH and the name (filename) of a song, returning the text of the song (song_text)
    # ----------------------------------------- WRITE HERE --------------------------------------------------

    url = image_search.perform_image_search(song_text) #this function can be found inside PythonGUI/APIs/select_music.py
    print(url)

    download_image.download_image(url,IMAGE_PATH) #this function can be found inside PythonGUI/APIs/select_music.py

    print("Process completed!")

    


if __name__ == "__main__":
    main()