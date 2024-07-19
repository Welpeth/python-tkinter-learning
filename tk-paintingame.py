import tkinter as tk
from tkinter import ttk

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = 'black')

brush_size = 4

window = tk.Tk()
window.geometry('500x300')
window.title('Painting Game')

canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0, min(brush_size, 50))

canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)


window.mainloop()