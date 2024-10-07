import datetime
from fastapi import FastAPI, Response, status
import os
import subprocess
import uvicorn
import pathlib
import sys

app = FastAPI() 

# Da sistemare cosa ritorna, deve essere un json
@app.get("/list-music", status_code=200)
def listMusic():
    currentDir = pathlib.Path(__file__).parent.resolve().as_posix()
    arr = os.listdir(currentDir+"/Music")
    return {"list-music": arr}

@app.get("/request-music", status_code=200)
def retrieveMusic(songName: str, dstPath: str, response: Response):
    currentDir = pathlib.Path(__file__).parent.resolve().as_posix()
    print(currentDir)
    if os.path.isfile(currentDir + "/Music/" + songName):
        if os.path.isdir(dstPath):
            subprocess.run("cp " + currentDir +"/Music/" + songName + " " + dstPath + "/song.mp3", shell = True, executable="/bin/bash")
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {404}
        return {200}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {404}

if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_config=log_config)