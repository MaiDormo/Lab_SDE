import requests


IMG_SEARCH_API_KEY= "AIzaSyAevW4pAAiZRODwx0nlhTGjVNZaJyB1Yl8"
CX= "f0e530b997279403d"


# Define endpoint
GOOGLE_SEARCH_URL = "https://www.googleapis.com/customsearch/v1"


# Perform Google image search based on transcribed text
def perform_image_search(query: str) -> (str | None):
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



