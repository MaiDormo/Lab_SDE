import requests


#URL of the API
URL = "http://127.0.0.1:8000/list-music"


def listAvailableMusic() -> list[str]:  
    """this function returns the list of available songs as a list of strings"""
    response = requests.get(URL).json() 
    return response["list-music"]