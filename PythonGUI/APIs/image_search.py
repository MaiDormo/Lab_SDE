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

    return results
    