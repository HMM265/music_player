import ast
import os
import tkinter
from tkinter import ttk
import threading
import wave
import time


#creating folders and saves
wav_music_folder = "./wav_music_folder" # Relative path

try:
    os.mkdir(wav_music_folder)
    print(f"Directory '{wav_music_folder}' created.")
except FileExistsError:
    print(f"Directory '{wav_music_folder}' already exists.")

file_name = "main_save.txt"

def save_value(input_value, filename):
    with open(filename, "w") as f:
        f.write(input_value)


def load_value(filename):
    with open(filename, "r") as f:
        read = f.read()
    return read

try:
    values = ast.literal_eval(load_value(file_name))
    print("Loaded values:", values)
except:
    print("Creating a new file...")
    values = {"color_mode": "light",
			  "screen_size": "small",}



#loading saved values
color_mode = values["color_mode"]
screen_size = values["screen_size"]

#important variables
layer = "Title"
music_file = 'music/bone-crunch-102701.wav'

running = True

chunk = 1024

	

#opening music
try:
    wf = wave.open(music_file, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    data = wf.readframes(chunk)
except:
    pass

#things with the screen
class Main_screen(tk.Tk):
    def __init__(self):
        super().__init__()

while running:
    pass


save_value(str(values), file_name)
t1.join()
stream.close()
p.terminate()