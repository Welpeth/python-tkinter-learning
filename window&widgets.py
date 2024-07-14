import tkinter as tk
from tkinter import ttk

def button_function():
    print('a button was pressed')

#def hello_func():
    #print ('Hello!')

# Criar janela
window = tk.Tk()
window.title('Janela e Widgets')
window.geometry('800x560')

# ttk label
label_titulo = ttk.Label(master = window, text = 'Olá!', font = 'Montserrat 24')
label_titulo.pack()

# tk text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# |------- Exercise ------- |

exercise_label = ttk.Label(master = window, text = 'my label', font = 'Montserrat 10')
exercise_label.pack()

# |------- Exercise ------- |

#ttk button
button = ttk.Button(master = window, text = 'Olá!', command = button_function)
button.pack()

# |------- Exercise ------- |

exercise_button = ttk.Button(master = window, text = 'Bem doido', command = lambda: print('hello'))
exercise_button.pack()

# |------- Exercise ------- |

# rodar
window.mainloop()