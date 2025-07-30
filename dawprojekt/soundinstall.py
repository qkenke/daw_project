import tkinter as tk
from tkinter import filedialog
import sounddevice as sd
import soundfile as sf
import os 

user_samples = []                                       # Samples that the user will add will be stored here

def play_sample(path):                                  #a function that plays samples
    data, samplerate = sf.read(path, dtype='int16')     #path = the path to audio file. data = array(sound). samplerate = sound frequency.
    sd.play(data, samplerate)                           #play sample                                   

def add_sound(frame):                                   #add sound that wants user
    filepath = filedialog.askopenfilename(              #opens the explorer and searches only for wav files
        title='Chose your file',
        filetypes =[
                ('WAV files', '*.wav')
        ])
    if filepath:                                        
        user_samples.append(filepath)                   #stored into array
        create_sample_button(filepath,frame)            #creates a button with a sample for playback

def create_sample_button(filepath, frame):              #create a button with sample
    filename = os.path.basename(filepath)               #takes only the file name
    button = tk.Button(frame, text = filename, command = lambda: play_sample(filepath))     
    button.pack() 

def open_window():

    window = tk.Toplevel()

    frame = tk.Frame(window)
    frame.pack()

    add_button = tk.Button(                            
        window, text = 'Add sound',
        command = lambda: add_sound(frame),
        font = ('Arial', 12)
    )
    add_button.pack(pady= 14 )

    window.title('STUDIO')
    window.geometry('400x300')
    

    stop_button = tk.Button(window, text = 'Stop sound', command = lambda: sd.stop, font = ('Arial', 12))
    stop_button.pack(pady= 30)

    window.mainloop()