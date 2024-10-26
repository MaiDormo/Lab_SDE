from fastapi.responses import FileResponse
from typing import Dict, Any
import requests
import os
import neuralspace as ns





#------------------------- 1 ----------------------
""" ❔
    1° Exercise:
    - define the correct URL to retrieve the list of music
"""

URL_LIST_MUSIC = "" #Insert the correct value inside this global variable.

# 💡 Hint:
# Keep in mind that the server is located at address 127.0.0.1 on port 8000
# and listening to HTTP request

def listAvailableMusic() -> list[str]:
    response = requests.get(URL_LIST_MUSIC).json()
    return response["list-music"]

#------------------------- 2 ----------------------
""" ❔
    2° Exercise:
    - define the correct URL to retrieve the required song
    - complete the code to make the request
"""

URL_REQUEST_MUSIC = "" #insert the URL in this global variable

# 💡 Hint:
# Take inspiration from the code and URL of previous exercise.


def importSong(requestedSong: str) -> (FileResponse | int):
    #TODO implement this function
    return

#------------------------- 3 ----------------------
# API key for STT
STT_API_KEY: str = "sk_a58a31d32bed7896a38ea55fa93fe8a1d709851e37e38c67e163c6004c9a0186"

# [Already implemented] 
def initialize_voice_ai() -> ns.VoiceAI:
    return ns.VoiceAI(api_key=STT_API_KEY)

""" ❔
    3° Exercise:
    - Complete the config with the correct values
"""

# 💡 Hint:
# 1. the "language" id is a two character string that identifies the language
#   - for example: "it" -> italian, "en" -> english, "de" -> "german", ...
# 2. the "mode" can be fast or advanced, depending on whether you want 
#   higher speed or higher accuracy.

# if one wishes here is the link to the doc 📃: 
# - https://voice.neuralspace.ai/docs/v2/file-transcription/overview

# Setup job configuration
def create_transcription_job(vai: ns.VoiceAI, filename: str) -> str:
    
    #TODO complete this config
    config= {
        'file_transcription': {
            'language_id': ,
            'mode': ,
        }
    }
    job_id = vai.transcribe(file=filename, config=config)
    print(f'Created job: {job_id}')
    return job_id

# [Already implemented] 
def extract_transcription_words(result: Dict[str, Any]) -> str:
    timestamps = result['data']['result']['transcription']['channels']['0']['timestamps']
    print(result)
    words = [entry['word'] for entry in timestamps]
    return " ".join(words)

#------------------------- 4 ----------------------

# API key for Image Search
IMG_SEARCH_API_KEY= "AIzaSyAevW4pAAiZRODwx0nlhTGjVNZaJyB1Yl8"

# Id of search engine
CX= "f0e530b997279403d"

# Define endpoint
GOOGLE_SEARCH_URL = "https://www.googleapis.com/customsearch/v1"


""" ❔
    4° Exercise:
    - Complete the config with the correct values
    - Complete the code to make the request
    - Collect the reponse as a JSON
"""

# 💡 1° Hint:
# Here is a brief description of each parameter that will be used:
# 1. "key" -> the API key (look above)
# 2. "cx" -> identifier of the programmable search engine (look above)
# 3. "q" -> the text query used in the search
# 4. "searchType" -> contains the search type, insert "image"
# 5. "num" -> number of search result to return
# 6. "filetype" -> Restricts results to files of a specified extension, 
#                  this can be "png", "jpeg", "gif" ...


# 💡 2° Hint:
# In order to perform request you can use the same request used in the first two exerecises.
# The get() function takes the URL and also parameters which will be encoded in the URL in the request.

# 💡 3° Hint:
# In order to convert the JSON reponse into a usable object we need to use a JSON Decoder
# The decoder can be used by calling the function json() on the requests, example:
#       r = requests.get('https://api.github.com/events')
#       r.json()




# Perform Google image search based on transcribed text
def perform_image_search(query: str) -> (str | None):
    
    #First request: complete the parameters
    params = {
        "key": ,
        "cx": ,
        "q": ,
        "searchType": ,
        "num": ,
        "fileType": 
    }

    full_url = f"https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={query}&searchType={}&num={}&fileType={}"
    
    #Second request: Make the request removing "None" with the correct call
    response = None

    if response.status_code == 200:
        
        #Third request: Decode the JSON response removing "None" with the correct call
        search_results = None
        
        print(search_results)
        
        if 'items' in search_results and search_results['items']:
            return search_results['items'][0]['link']
        else:
            print("No image results found.")
            return None
    else:
        print(f"Failed to fetch search results. Status code: {response.status_code}")
        return None

#------------------------- 5 ----------------------

""" ❔
    5° Exercise:
    - Complete the code to make the request, in order to download the image
"""

# 💡 Hint:
#   If you make a get request on a given url you can get the content of the url.
#   So you need to make the request with the image_url and extract the content.
#   This can be done by adding .content() at the end of the call code.


# Downloads image to a defined save_path
def download_image(image_url: str, save_path: str):
    try:
        img_data = None
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as handler:
            handler.write(img_data)
        print(f"Image downloaded and saved at {save_path}")
    except Exception as e:
        print(f"Failed to download image: {e}")
