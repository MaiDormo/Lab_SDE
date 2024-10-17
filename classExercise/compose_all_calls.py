from fastapi.responses import FileResponse
from typing import Dict, Any
import requests
import os
import neuralspace as ns

URL_LIST_MUSIC = "http://127.0.0.1:8000/list-music"
URL_REQUEST_MUSIC = "http://127.0.0.1:8000/request-music"

# API key for STT
STT_API_KEY: str = "sk_a58a31d32bed7896a38ea55fa93fe8a1d709851e37e38c67e163c6004c9a0186"

# API key for Image Search
IMG_SEARCH_API_KEY= "AIzaSyAevW4pAAiZRODwx0nlhTGjVNZaJyB1Yl8"
# Id of search engine
CX= "f0e530b997279403d"

# Define endpoint
GOOGLE_SEARCH_URL = "https://www.googleapis.com/customsearch/v1"

"""
How this code is going to be structured:
    1. function to show songs -> just definition not body
    2. function to request a song -> just definition not body
    3. function to sumbit a job for STT -> just let them configure the job and make a request
    4. function to sumbit make a image search -> let them configure the params and let them make the request
"""
#the function to download the image will be give
#If parsing of the JSON response is to difficult give some help to the students.


#------------------------- 1 ----------------------

def listAvailableMusic() -> list[str]:
    #TODO implement this function
    return

#------------------------- 2 ----------------------

def importSong(requestedSong) -> (FileResponse | int):
    #TODO implement this function
    return

#------------------------- 3 ----------------------

# [Already implemented] 
def initialize_voice_ai() -> ns.VoiceAI:
    return ns.VoiceAI(api_key=STT_API_KEY)

# Setup job configuration
def create_transcription_job(vai: ns.VoiceAI, filename: str) -> str:
    
    #TODO complete this config
    config= {
        """
        'file_transcription': {
            'language_id': ,
            'mode': ,
        }
        """
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

# Perform Google image search based on transcribed text
def perform_image_search(query: str) -> (str | None):
    #complete the parameters
    params = {
       """ 
        "key": ,
        "cx": ,
        "q": ,
        "searchType": ,
        "num": ,
        "fileType": 
        """
    }
    
    #make the request
    response = None
    #----

    if response.status_code == 200:
        
        #get the json from the response
        search_results = None
        #----
        
        print(search_results)
        
        if 'items' in search_results and search_results['items']:
            return search_results['items'][0]['link']
        else:
            print("No image results found.")
            return None
    else:
        print(f"Failed to fetch search results. Status code: {response.status_code}")
        return None


# [Already implemented] Downloads image to a defined save_path
def download_image(image_url: str, save_path: str):
    try:
        img_data = requests.get(image_url).content
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as handler:
            handler.write(img_data)
        print(f"Image downloaded and saved at {save_path}")
    except Exception as e:
        print(f"Failed to download image: {e}")
