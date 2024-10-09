import datetime
import tkinter as tk
from tkinter import ttk
import os, subprocess
from PIL import ImageTk, Image
from APIs import list_music, select_music, lab_SDE_2024
import pathlib

class ModernMusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Processing App")
        self.root.geometry('900x700')
        self.root.configure(bg='#f0f0f0')
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', 
                            padding=10, 
                            font=('Helvetica', 10),
                            background='#0066cc',
                            foreground='white')
        self.style.map('TButton',
                       background=[('active', '#0052a3')])
        self.style.configure('TLabel', 
                            background='#f0f0f0', 
                            font=('Helvetica', 10))
        self.style.configure('Header.TLabel', 
                            font=('Helvetica', 14, 'bold'))
        
        self.create_widgets()

    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Step 1: Show available songs
        step1_frame = self.create_section_frame(main_frame, "Step 1: Available Songs", 0)
        ttk.Button(step1_frame, text="Show Songs", command=self.show_songs).grid(row=0, column=0, pady=5)
        self.song_listbox = tk.Listbox(step1_frame, height=5, width=40, font=('Helvetica', 10))
        self.song_listbox.grid(row=1, column=0, pady=5)
        
        # Step 2: Import song
        step2_frame = self.create_section_frame(main_frame, "Step 2: Import Song", 1)
        entry_frame = ttk.Frame(step2_frame)
        entry_frame.grid(row=0, column=0, pady=5)
        self.song_entry = ttk.Entry(entry_frame, width=30, font=('Helvetica', 10))
        self.song_entry.grid(row=0, column=0, padx=5)
        ttk.Button(entry_frame, text="Import", command=self.import_song).grid(row=0, column=1, padx=5)
        self.import_status = ttk.Label(step2_frame, text="", font=('Helvetica', 10))
        self.import_status.grid(row=1, column=0, pady=5)
        
        # Step 3: Extract text
        step3_frame = self.create_section_frame(main_frame, "Step 3: Extract Text", 2)
        ttk.Button(step3_frame, text="Extract Text", command=self.extract_text).grid(row=0, column=0, pady=5)
        self.text_display = tk.Text(step3_frame, height=4, width=40, font=('Helvetica', 10), wrap=tk.WORD)
        self.text_display.grid(row=1, column=0, pady=5)
        
        # Step 4: Search image
        step4_frame = self.create_section_frame(main_frame, "Step 4: Search Image", 3)
        ttk.Button(step4_frame, text="Search Image", command=self.search_text).grid(row=0, column=0, pady=5)
        self.image_frame = ttk.Frame(step4_frame, width=400, height=300)
        self.image_frame.grid(row=1, column=0, pady=10)
        self.image_frame.grid_propagate(False)
        self.image_label = ttk.Label(self.image_frame)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_section_frame(self, parent, title, row):
        frame = ttk.Frame(parent, padding="10")
        frame.grid(row=row, column=0, sticky=(tk.W, tk.E), pady=10)
        ttk.Label(frame, text=title, style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        content_frame = ttk.Frame(frame)
        content_frame.grid(row=1, column=0)
        return content_frame

    def show_songs(self):
        self.song_listbox.delete(0, tk.END)
        try:
            songs = list_music.listAvailableMusic()
            for song in songs:
                self.song_listbox.insert(tk.END, song)
        except Exception as e:
            self.song_listbox.insert(tk.END, f"Error: {str(e)}")

    def import_song(self):
        song_name = self.song_entry.get()
        if not song_name:
            self.update_status("Please enter a song name", "red")
            return
        
        try:
            ret_val = select_music.importSong(song_name)
            
            if ret_val != 1:
                current_folder = pathlib.Path(__file__).parent.resolve().as_posix()
                open(current_folder + '/song.mp3', 'wb').write(ret_val.content)
                self.update_status(f"{song_name} successfully imported!", "green")
            else:
                self.update_status(f"{song_name} does not exist!", "red")
        except Exception as e:
            self.update_status(f"Error: {str(e)}", "red")

    def extract_text(self):
        current_folder = pathlib.Path(__file__).parent.resolve().as_posix()
        try:
            vai = lab_SDE_2024.initialize_voice_ai()
            job_id = lab_SDE_2024.create_transcription_job(vai, current_folder + "/song.mp3")
            result = vai.poll_until_complete(job_id)
            song_text = lab_SDE_2024.extract_transcription_words(result)
            
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, song_text)
        except Exception as e:
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, f"Error: {str(e)}")

    def search_text(self):
        try:
            text = self.text_display.get(1.0, tk.END).strip()
            if not text:
                return
            
            image_url = lab_SDE_2024.perform_image_search(text)
            if image_url:
                image_save_path = os.path.join("images", "downloaded_image.png")
                lab_SDE_2024.download_image(image_url, image_save_path)
                self.display_image(image_save_path)
        except Exception as e:
            print(f"Error searching/displaying image: {str(e)}")

    def display_image(self, image_path):
        try:
            pil_image = Image.open(image_path)
            pil_image.thumbnail((380, 280))
            photo = ImageTk.PhotoImage(pil_image)
            
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error displaying image: {str(e)}")

    def update_status(self, message, color):
        self.import_status.config(text=message, foreground=color)

def main():
    
    root = tk.Tk()
    app = ModernMusicApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()