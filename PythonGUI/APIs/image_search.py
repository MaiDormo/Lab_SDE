from duckduckgo_search import DDGS


def perform_image_search(query: str) -> (str | None):
    """Perform DuckDucKGo image search based on transcribed text"""
    results = None
    try:
        results = DDGS().images(
                keywords=query,
                region="wt-wt",
                safesearch="moderate",
                max_results=1,
            )
    except:
        print("Error in requesting the image")

    if results and len(results) > 0:
        # Estrai l'URL dell'immagine dal primo risultato
        image_url = results[0].get('image', None)  # Cambia 'image' se la chiave è diversa
        return image_url
    return None
    
