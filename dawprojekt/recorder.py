import sounddevice as sd
from scipy.io.wavfile import write 
import numpy as np 
import datetime 
import tkinter as tk 
import os

samplerate= 44100                                           #frequency.the higher the frequency, the greater the accuracy of the sound
channels = 1                                                #sound in mono.(Sound in mono = 1, in stereo = 2)
recording_data = []                                         #files where we store recordings
recording = False                                                   

save_folder = 'recordings'                                  #name of floder 
os.makedirs(save_folder,exist_ok=True)                      #create one folder where will the recordings be sent.
                                                            #Exist.ok = does not return an error, when folder exist

def callback(indata, frames, time, status):                 #There are so many arguments because sounddevice accepts this signature.
    if recording: 
        recording_data.append(indata.copy())                #indata = microphone signal. copy becouse indata is changing.and the audio may be distorted.
    
def start_rec():    
    global recording, stream, recording_data
    recording_data = []                                     #recording_data like white canvas. We using it for store wav files each one separetaly                   
    recording = True 
    stream = sd.InputStream(callback = callback, samplerate = samplerate, channels = 1, dtype = 'int16')#what characteristics will the audio have 
    stream.start() 

def stop_rec():
    global recording 
    recording = False 
    stream.stop() 
    stream.close() 
    if recording_data:
        audio = np.concatenate(recording_data)                              #we collect everything in one array becouse еhe microphone sends sound in parts.
                                                                            #the file may become corrupted
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')       #names of files
        filename = f'recording_{timestamp}.wav'                             #what file will be look like
        filename = os.path.join(save_folder, filename)                      #path to folder
        write(filename,samplerate,audio)
        print('Stored in a folder')
        return filename
    else:
        print('No data to record')
        return None

def open_window():                                                          #Gui settings
    window = tk.Toplevel() 
    window.title('Rec')                                                     
    window.geometry('300x200')                                              #size of window

    start_button = tk.Button(window,text = 'start', command = start_rec, font=('Arial',10)) #button to start recording
    start_button.pack(pady = 10)

    stop_button = tk.Button(window,text = 'stop', command = stop_rec, font=('Arial',10))    #button to stop recording
    stop_button.pack(pady=20)

    window.mainloop()                                                       #launch the window