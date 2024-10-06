from tkinter import *
import os
from APIs import list_music, select_music, lab_SDE_2024
import pathlib
from PIL import ImageTk, Image

root = Tk()
root.title("Lab3 API GUI")
root.geometry('800x600')

MusicArr = []

## Functions definition
def show_songs():
    MusicArr = list_music.listAvailableMusic()
    newText = ""

    for song in MusicArr:
        newText += "- " + song + "\n"

    musicList.config(text=newText)

def import_songs():
    currentFolder = pathlib.Path().resolve().as_posix()
    requestedSong = writeMusic.get()
    retVal = select_music.importSong(requestedSong, currentFolder)
    if retVal == 0:
        step1_output.config(text=requestedSong+" successfully imported!", fg="#000000")
    else:
        step1_output.config(text=requestedSong+" does not exist!", fg="#ff5733")

def extract_text():
    vai = lab_SDE_2024.initialize_voice_ai()

    # Create and poll transcription job
    job_id = lab_SDE_2024.create_transcription_job(vai, "./song.mp3")
    print('Waiting for completion...')
    result = vai.poll_until_complete(job_id)

    # Extract the transcribed text
    song_text = lab_SDE_2024.extract_transcription_words(result)

    step2_output.config(text=song_text)

def search_text():
    # Perform image search based on transcribed text
    image_url = lab_SDE_2024.perform_image_search(step2_output.cget("text"))

    if image_url:
        # Download the image
        image_save_path = os.path.join("images", "downloaded_image.jpg")
        lab_SDE_2024.download_image(image_url, image_save_path)
        panel.pack()
##

## GUI 
step0 = Label(root, text="STEP 0: Show available songs", font='Helvetica 18 bold')
step0.grid(row=0)

Button(root, text="Show songs", command=show_songs).grid(column=1, row=1)

musicList = Label(root, text="", font='Helvetica 12')
musicList.grid(column=1, row=2)

step1 = Label(root, text="STEP 1: Import selected music", font='Helvetica 18 bold')
step1.grid(row=3)

writeMusic = Entry(root, width=10)
writeMusic.grid(column=1, row=4)

Button(root, text="Import song", command=import_songs).grid(column=1, row=5)

step1_output = Label(root, font='Helvetica 18 bold')
step1_output.grid(column=2, row=5)

step2 = Label(root, text="STEP 2: Extract text from music", font='Helvetica 18 bold')
step2.grid(row=6)

Button(root, text="Extract Text", command=extract_text).grid(column=1, row=7)

step2_output = Label(root, font='Helvetica 18 bold')
step2_output.grid(column=1, row=8)

step3 = Label(root, text="STEP 3: Google search from text", font='Helvetica 18 bold')
step3.grid(row=9)

Button(root, text="Google search", command=search_text).grid(column=1, row=10)

# DA PROVARE
# img = ImageTk.PhotoImage(Image.open("./downloaded_image.jpg"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# panel.pack_forget()
# panel.grid(column=1, row=11)
##

root.mainloop()