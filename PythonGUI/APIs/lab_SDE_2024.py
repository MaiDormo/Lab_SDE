import neuralspace as ns
import requests
import os

# STT_API_KEY = os.environ.get('STT_API_KEY')
# IMG_SEARCH_API_KEY = os.environ.get('IMG_SEARCH_API_KEY')
# CX = os.environ.get('CX')

STT_API_KEY = "sk_a58a31d32bed7896a38ea55fa93fe8a1d709851e37e38c67e163c6004c9a0186"
IMG_SEARCH_API_KEY= "AIzaSyAevW4pAAiZRODwx0nlhTGjVNZaJyB1Yl8"
CX= "f0e530b997279403d"


# Define endpoint and filename
GOOGLE_SEARCH_URL = "https://www.googleapis.com/customsearch/v1"
AUDIO_FILE_PATH = './example_audio.mp3'

# Initialize VoiceAI with API key
def initialize_voice_ai():
    return ns.VoiceAI(api_key=STT_API_KEY)

# Setup job configuration
def create_transcription_job(vai, filename):
    config = {
        'file_transcription': {
            'language_id': 'en',
            'mode': 'advanced',
        }
    }
    job_id = vai.transcribe(file=filename, config=config)
    print(f'Created job: {job_id}')
    return job_id

# Extract words from transcription result
def extract_transcription_words(result):
    timestamps = result['data']['result']['transcription']['channels']['0']['timestamps']
    print(result)
    words = [entry['word'] for entry in timestamps]
    return " ".join(words)

# Perform Google image search based on transcribed text
def perform_image_search(query):
    params = {
        "key": IMG_SEARCH_API_KEY,
        "cx": CX,
        "q": query,
        "searchType": "image",
        "num": 1,
        "fileType": "png"
    }
    response = requests.get(GOOGLE_SEARCH_URL, params=params)
    if response.status_code == 200:
        search_results = response.json()
        print(search_results)
        if 'items' in search_results and search_results['items']:
            return search_results['items'][0]['link']
        else:
            print("No image results found.")
            return None
    else:
        print(f"Failed to fetch search results. Status code: {response.status_code}")
        return None

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

# Main function to handle the process
def main():
    vai = initialize_voice_ai()
    
    # Create and poll transcription job
    job_id = create_transcription_job(vai, AUDIO_FILE_PATH)
    print('Waiting for completion...')
    result = vai.poll_until_complete(job_id)
    
    # Extract the transcribed text
    song_text = extract_transcription_words(result)
    print(f"Transcribed Text: {song_text}")
    
    # Perform image search based on transcribed text
    image_url = perform_image_search(song_text)
    
    if image_url:
        # Download the image
        image_save_path = os.path.join("images", "downloaded_image.jpg")
        download_image(image_url, image_save_path)

if __name__ == "__main__":
    main()