import requests

URL = "http://127.0.0.1:8000/list-music"

response = requests.get(URL).json()

for song in response["list-music"]:
    print(song)