import requests
URL = "http://127.0.0.1:8000/request-music"

requestedSong = input()
dstFolder = input()

PARAMS = {'songName':requestedSong, 'dstPath':dstFolder}

response = requests.get(URL, PARAMS)

print(response.text)