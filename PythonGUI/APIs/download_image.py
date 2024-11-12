import os
import requests

def download_image(image_url: str, save_path: str):
    """
    Download the image from the provided URL and save it to the specified path.
    
    Args:
        image_url (str): The URL of the image to be downloaded.
        save_path (str): The directory path where the image will be saved.
    """
    try:
        # Send a GET request to the image URL and get the content of the response
        img_data = requests.get(image_url).content
        
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Open the specified file path in write-binary mode and write the image data to it
        with open(save_path, 'wb') as handler:
            handler.write(img_data)
        
        # Print a success message with the save path
        print(f"Image downloaded and saved at {save_path}")
    except Exception as e:
        # Print an error message if the download fails
        print(f"Failed to download image: {e}")