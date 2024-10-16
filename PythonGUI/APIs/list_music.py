import requests

URL = "http://127.0.0.1:8000/list-music"

def listAvailableMusic() -> list[str]:
    response = requests.get(URL).json()
    return response["list-music"]