import neuralspace as ns
from typing import Dict, Any

# API key for Speech-to-Text (STT) service
STT_API_KEY: str = "sk_a58a31d32bed7896a38ea55fa93fe8a1d709851e37e38c67e163c6004c9a0186"

def initialize_voice_ai() -> ns.VoiceAI:
    """
    Initialize VoiceAI Object with API key.
    
    Returns:
        ns.VoiceAI: The initialized VoiceAI object.
    """
    # Initialize the VoiceAI object using the provided API key
    return ns.VoiceAI(api_key=STT_API_KEY)

def create_transcription_job(vai: ns.VoiceAI, filename: str) -> str:
    """
    Setup job configuration and create a transcription job.
    
    Args:
        vai (ns.VoiceAI): The initialized VoiceAI object.
        filename (str): The name of the song file.
    
    Returns:
        str: The job ID of the created transcription job.
    """
    # Configuration for the transcription job
    config = {
        'file_transcription': {
            'language_id': 'en',  # Set the language to English
            'mode': 'advanced',   # Set the mode to advanced
        }
    }
    # Create a transcription job with the specified file and configuration
    job_id = vai.transcribe(file=filename, config=config)  # This is a library wrapper function that makes the actual HTTP request
    print(f'[CREATED JOB]: {job_id}')
    # Return the job_id that will later be checked to understand the status of the transcription job
    return job_id

def extract_transcription_words(result: Dict[str, Any]) -> str:
    """
    Extract words from transcription result by parsing the result JSON.
    
    Args:
        result (Dict[str, Any]): The result of the transcription job.
    
    Returns:
        str: The extracted words concatenated with a single space (" ").
    """
    # Print the result for debugging purposes
    print(f"[STT RESULT]: {result}")
    # Extract all timestamps from the transcription result
    timestamps = result['data']['result']['transcription']['channels']['0']['timestamps']
    # Gather all words from the timestamps
    words = [entry['word'] for entry in timestamps]
    # Return all words concatenated with a single space (" ")
    return " ".join(words)