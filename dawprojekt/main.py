import tkinter as tk 
import recorder as rc 
import soundinstall as si 

def open_recorder():
    rc.open_window()

def open_soundinstall():
    si.open_window()

window = tk.Tk()
window.title('STUDIO')
window.geometry('300x200')
window.configure(bg="#616494") 

window.update_idletasks()
width = 400
height = 250
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f'{width}x{height}+{x}+{y}')

title = tk.Label(window, text = 'Studio',font = ('Arial',20,'bold'), fg = 'white', bg="#2c2952")

button_style = {
    'font': ('Arial', 14),
    'bg': "#322a50",
    'fg': 'white',
    'activebackground': "#3B3988",
    'activeforeground': 'white',
    'relief': 'flat',
    'width': 15
}

tk.Button(window, text = 'Start rec', command = open_recorder, **button_style).pack(pady = 10)
tk.Button(window, text = 'Add sample', command = open_soundinstall, **button_style).pack(pady = 10)

window.mainloop()