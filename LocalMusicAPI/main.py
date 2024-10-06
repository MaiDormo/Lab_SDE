from fastapi import FastAPI, Response, status
import os
import subprocess

app = FastAPI() 

# Da sistemare cosa ritorna, deve essere un json
@app.get("/list-music", status_code=200)
def listMusic():
    retVal = ""
    arr = os.listdir("./Music")
    return {"list-music": arr}

@app.get("/request-music", status_code=200)
def retrieveMusic(songName: str, dstPath: str, response: Response):
    if os.path.isfile("./Music/" + songName + ".mp3"):
        if os.path.isdir(dstPath):
            subprocess.run("cp ./Music/" + songName + ".mp3 " + dstPath + "/song.mp3", shell = True, executable="/bin/bash")
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {404}
        return {200}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {404}