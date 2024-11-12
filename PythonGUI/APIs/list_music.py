import requests

# URL of the API endpoint to list available music
URL = "http://127.0.0.1:8000/list-music"

def listAvailableMusic() -> list[str]:
    """
    Returns the list of available songs as a list of strings.
    
    Returns:
        list[str]: A list of available song names.
    """
    # Send a GET request to the API endpoint and parse the JSON response
    response = requests.get(URL).json()
    
    # Return the list of available music from the response
    return response["list-music"]