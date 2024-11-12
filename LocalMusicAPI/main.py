from fastapi import FastAPI, Response, status
from fastapi.responses import FileResponse
from typing import Union
import os
import uvicorn
import pathlib


MUSIC_FOLDER = "/Music/" #folder from which the Local APIs take the songs

app = FastAPI() 


@app.get("/list-music", status_code=200)
def listMusic() -> dict[str, list[str]]:
    """Local API that lists all of the available song from the folder"""
    currentDir = pathlib.Path(__file__).parent.resolve().as_posix()
    arr = os.listdir(currentDir + MUSIC_FOLDER)
    return {"list-music": arr}

@app.get("/request-music", status_code=200, response_model=None)
def retrieveMusic(songName: str, response: Response) -> Union[FileResponse, dict[str, int]]:
    """Local API that retrieves the song given the songName"""
    currentDir = pathlib.Path(__file__).parent.resolve().as_posix()
    checkPath = currentDir + MUSIC_FOLDER + songName
    if os.path.isfile(checkPath):
        return FileResponse(checkPath, media_type="audio/mpeg", filename="song.mp3")
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status_code": 404}

if __name__ == "__main__":
    #logging configuration for the terminal
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_config=log_config)