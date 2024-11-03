import os
import requests

def download_image(image_url: str, save_path: str):
    """Download the image from the provided URL in the save_path folder"""
    try:
        img_data = requests.get(image_url).content
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as handler:
            handler.write(img_data)
        print(f"Image downloaded and saved at {save_path}")
    except Exception as e:
        print(f"Failed to download image: {e}")