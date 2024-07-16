import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('500x500')
window.title('Combobox & Spinbox')

#Widgets
#Combobox
items = ('Ice Cream', 'Pizza', 'Brocoli')

food_string = tk.StringVar(value = items[0])

combobox = ttk.Combobox(window, textvariable = food_string)
combobox['values'] = items
combobox.pack()

#events
combobox.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

#spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(window, from_ = 3, to = 20, increment = 3, textvariable = spin_int, command = lambda: print(spin_int.get()))

spin.bind('<<Increment>>', lambda event: print('Up'))
spin.bind('<<Decrement>>', lambda event: print('Down'))

spin.pack()

#exercise

items = ('A', 'B', 'C', 'D', 'E')

letter_string = tk.StringVar(value = items[0])
spin = ttk.Spinbox(window, textvariable = letter_string, values = items)
spin.pack()

spin.bind('<<Decrement>>', lambda event: print(letter_string.get()))

window.mainloop()