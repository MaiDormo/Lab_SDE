import os
import requests

# Download the image from the provided URL
def download_image(image_url, save_path):
    try:
        img_data = requests.get(image_url).content
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as handler:
            handler.write(img_data)
        print(f"Image downloaded and saved at {save_path}")
    except Exception as e:
        print(f"Failed to download image: {e}")