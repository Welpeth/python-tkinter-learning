import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Botões')
window.geometry('600x400')

# buttons
def button_func():
    print('simple button')

#string_button = tk.StringVar(value = 'a button with stringvar')
#button = ttk.Button(window, text = 'Esse botão é legal', command = lambda: print('Olá mundo'), textvariable = string_button)
#button.pack()

# check button
#check_var = tk.IntVar(value = 10)
#check = ttk.Checkbutton(window, text = 'checkbox 1', command = lambda: print(check_var.get()), variable = check_var, onvalue = 10, offvalue = 5)
#check.pack()

#radio button
#radio_var = tk.StringVar()

#radio1 = ttk.Radiobutton(window, text = 'Radiobutton 1', variable = radio_var, value = 'radio 1', command = lambda: print(radio_var.get()))
#radio1.pack()

#radio2 = ttk.Radiobutton(window, text = 'Radiobutton 2', variable = radio_var, value = 2)
#radio2.pack()

#exercise

check_var = tk.BooleanVar()
radio1_var = tk.StringVar(value = 'A')
radio2_var = tk.StringVar(value = 'B')

exercise_check = ttk.Checkbutton(window, text = 'This is a checkbox', variable = check_var, command = lambda: print(radio1_var.get() or radio2_var.get()))
exercise_check.pack()

exercise_radio1 = ttk.Radiobutton(window, text = 'This is a radio button', value = 'doido', variable = radio1_var, command = lambda: print(check_var.get()), onvalue = check_var)
exercise_radio1.pack()

exercise_radio2 = ttk.Radiobutton(window, text = 'This is a radio button', value = 1, variable = radio2_var, command = lambda: print(check_var.get()), onvalue = check_var)
exercise_radio2.pack()


window.mainloop()