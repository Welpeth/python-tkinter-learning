import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

window = tk.Tk()
window.title('Event Binding')
window.geometry('700x700')

#widgets

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = 'Button')
btn.pack()

#events

btn.bind('<Alt-KeyPress-a>', lambda event: print(event))
window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))
window.bind('<Motion>', get_pos)

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

#Exercise

text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

#run 
window.mainloop()