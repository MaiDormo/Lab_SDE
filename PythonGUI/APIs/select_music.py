import requests
URL = "http://127.0.0.1:8000/request-music"

def importSong(requestedSong):
    PARAMS = {'songName':requestedSong}
    response = requests.get(URL, PARAMS)
    if response.status_code == 200:
        return response
    else:
        return 1