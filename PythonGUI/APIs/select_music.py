import requests
from fastapi.responses import FileResponse

# URL of the API endpoint to request a specific music file
URL = "http://127.0.0.1:8000/request-music"

def importSong(requestedSong: str) -> (FileResponse | int):
    """
    This function returns a FileResponse (the actual mp3 file of the song)
    if the name inserted is correct, otherwise this function will return 1.
    
    Args:
        requestedSong (str): The name of the song to be requested.
    
    Returns:
        FileResponse: The response containing the mp3 file if the song name is correct.
        int: Returns 1 if the song name is incorrect or the request fails.
    """
    
    # Parameters to be sent in the GET request
    PARAMS = {'songName': requestedSong}
    
    # Send a GET request to the API endpoint with the specified parameters
    response = requests.get(URL, PARAMS)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the response containing the mp3 file
        return response
    else:
        # Return 1 if the request fails
        return 1