import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

#Window
window = tk.Tk()
window.title('Variaveis Tkinter')
window.geometry('300x150')

#Tkinter variavel
string_var = tk.StringVar()

# Widgets
label = ttk.Label(master = window, text = 'Tkinter Variables', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = "button", command = button_func)
button.pack()

#exercise

#variavelteste = tk.StringVar(value = 'test')

#exercise_label = ttk.Label(master = window, text = "Olá mundo", textvariable = variavelteste)
#exercise_label.pack()

#exercise_entry = ttk.Entry(master = window, textvariable = variavelteste)
#exercise_entry.pack()

#exercise_entry2 = ttk.Entry(master = window, textvariable = variavelteste)
#exercise_entry2.pack()

window.mainloop()