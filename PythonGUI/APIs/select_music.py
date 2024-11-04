import requests
from fastapi.responses import FileResponse 

#URL of the API
URL = "http://127.0.0.1:8000/request-music"


def importSong(requestedSong: str) -> (FileResponse | int):
    """ This function returns a fileResponse (the actual mp3 file of the song),
    if the name inserted is correct, otherwise this function will return 1 """
    
    PARAMS = {'songName':requestedSong}
    response = requests.get(URL, PARAMS)
    if response.status_code == 200:
        return response
    else:
        return 1