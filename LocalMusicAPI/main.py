from fastapi import FastAPI, Response, status
from fastapi.responses import FileResponse
import os
import uvicorn
import pathlib

app = FastAPI() 

@app.get("/list-music", status_code=200)
def listMusic():
    currentDir = pathlib.Path(__file__).parent.resolve().as_posix()
    arr = os.listdir(currentDir+"/Music")
    return {"list-music": arr}

@app.get("/request-music", status_code=200)
def retrieveMusic(songName: str, response: Response):
    currentDir = pathlib.Path(__file__).parent.resolve().as_posix()
    if os.path.isfile(currentDir + "/Music/" + songName):
        return FileResponse(currentDir + "/Music/" + songName, media_type="audio/mpeg", filename="song.mp3")
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {404}

if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_config=log_config)