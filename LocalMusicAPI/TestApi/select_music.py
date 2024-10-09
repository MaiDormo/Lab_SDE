import requests
URL = "http://127.0.0.1:8000/request-music2"

requestedSong = "BohemianRhapsody.mp3"

PARAMS = {'songName':requestedSong}

response = requests.get(URL, PARAMS)

open('song.mp3', 'wb').write(response.content)