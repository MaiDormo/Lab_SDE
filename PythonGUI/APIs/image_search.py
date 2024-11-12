from duckduckgo_search import DDGS

def perform_image_search(query: str) -> (str | None):
    """
    Perform DuckDuckGo image search based on transcribed text.
    
    Args:
        query (str): The search query string.
    
    Returns:
        str | None: The URL of the first image result, or None if no results are found.
    """
    results = None
    try:
        # Perform an image search using DuckDuckGo with the specified query
        results = DDGS().images(
            keywords=query,  # Search keywords
            max_results=1,   # Limit the results to 1 image
        )
    except Exception as e:
        # Print an error message if the search request fails
        print(f"Error in requesting the image: {e}")

    # Return the URL of the first image result
    print(f"[IMAGE SEARCH RESULT]: {results}")
    return results[0]["image"] if results else None