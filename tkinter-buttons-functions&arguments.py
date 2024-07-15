import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('UAU')
window.geometry('300x300')

def button_func(entry_string):
    print('Um botão foi apertado')
    print(entry_string.get())

# Widgets
entry_string = tk.StringVar(value = 'text')
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

button = ttk.Button(window, text = 'Olá mundo', command = lambda: button_func(entry_string))
button.pack()

window.mainloop()