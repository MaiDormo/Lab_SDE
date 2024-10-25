import requests
from fastapi.responses import FileResponse 

URL = "http://127.0.0.1:8000/request-music"

def importSong(requestedSong: str) -> (FileResponse | int):
    PARAMS = {'songName':requestedSong}
    response = requests.get(URL, PARAMS)
    if response.status_code == 200:
        return response
    else:
        return 1