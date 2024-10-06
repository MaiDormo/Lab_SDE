import requests
URL = "http://127.0.0.1:8000/request-music"

def importSong(requestedSong, dstFolder):
    PARAMS = {'songName':requestedSong, 'dstPath':dstFolder}
    response = requests.get(URL, PARAMS)
    if response.status_code == 200:
        return 0
    else:
        return 1