import tkinter as tk
from tkinter import ttk

#functions

def button_func():
    entry_text = entry.get()
    label['text'] = entry_text
    entry ['state'] = 'disabled'

def exercise_button():
    label['text'] = 'some text'
    entry ['state'] = 'enabled'

#window

window = tk.Tk()
window.title('Setando e modificando widgets')
window.geometry('300x100')

#widgets

label = ttk.Label(master = window, text = 'Aprendendo TKINTER!', font = 'Montserrat 10')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'press', command = button_func)
button.pack()

exercise_button = ttk.Button(master = window, text = 'exercise button', command = exercise_button)
exercise_button.pack()

window.mainloop()