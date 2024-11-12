from API_Output_Manipulation import functions
from fastapi.responses import FileResponse
import pathlib
import sys

# Add the PythonGUI directory to the system path for module imports
sys.path.append('./PythonGUI')
from APIs import download_image, image_search, list_music, select_music

# You have available the following functions
# ----------------------------------------------------------------------------------------------------------------------------------------------
# download_image.download_image()           Given as input the URL of the image and the path where to save it, downloads an image from the internet
# image_search.perform_image_search()       Given a string with the content to search on the internet, returns the URL of an image found
# list_music.listAvailableMusic()           Returns a list with all the names of the songs available for import (strings)
# select_music.importSong()                 Given a string with the name of the song, returns a FileResponse that contains a file with that song

# functions.download_image()                Given an image URL and a path, downloads that image in the specified path
# functions.extract_song()                  Given a FileResponse and a path, downloads the song in the specified path
# functions.speech_to_text()                Given the path to a song and the generated name for the extracted song, extracts its lyrics
# ----------------------------------------------------------------------------------------------------------------------------------------------

# Constants used to specify the paths of songs and images
SONG_PATH = pathlib.Path(__file__).parent.resolve().as_posix()  # Represents the folder location to which the song will be exported.
IMAGE_PATH = SONG_PATH + "/images/downloaded_image.png"  # Represents the template path where the image will be downloaded.





"""
Sequence of API calls:
1. list of available songs -> 2. import the first song -> 3. extract the song -> 4. convert the song to text -> 
 -> 5. perform an image search -> 3. download the image

In LAB Exercise:
    - You need to add the underlined two lines of code in order to make the whole main function work,
      thus completing all of the API calls shown before.
"""

def main():
    # Step 1: List all available songs
    song_list = list_music.listAvailableMusic()  # This function can be found inside PythonGUI/APIs/list_music.py
    print(f" [SONG LIST]: {song_list}")

    # Step 2: Import the first song from the list
    selected_song = select_music.importSong(song_list[0])  # This function can be found inside PythonGUI/APIs/select_music.py

    # Step 3: Extract the song to the specified path
    # Insert a call to the function extract_song() which can be found inside the functions.py file
    # It takes as input a song (FileResponse) and the SONG_PATH, and returns a filename
    filename = functions.extract_song(selected_song, SONG_PATH)

    # Step 4: Convert the song to text (lyrics)
    # Insert a call to the function speech_to_text() which can be found inside the API_Output_Manipulation/functions.py file
    # It takes as input the SONG_PATH and the name (filename) of the song, returning the text of the song (song_text)
    song_text = functions.speech_to_text(SONG_PATH, filename)

    # Step 5: Perform an image search based on the extracted text
    url = image_search.perform_image_search(song_text)  # This function can be found inside PythonGUI/APIs/image_search.py
    print(f"[IMAGE URL]: {url}")

    # Step 6: Download the image from the URL obtained
    download_image.download_image(url, IMAGE_PATH)  # This function can be found inside PythonGUI/APIs/download_image.py

    print("Process completed!")

if __name__ == "__main__":
    main()