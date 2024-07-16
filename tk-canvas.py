import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.geometry('600x600')
window.title('Canvas')

#widget
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()



#--Retangulo--:

#canvas.create_rectangle(('left, top, right, bottom'))

#--Exemplo:
canvas.create_rectangle((50, 20, 100, 200), fill = 'red', width = 1, dash = (2,4), outline = 'green')



#--Linha--:

#canvas.create_line(start_x, start_y, end_x, end_y)

#--Exemplo:
canvas.create_line((0, 0, 100, 150), fill = 'blue')



#--Circulo--:

#canvas.create_oval(left, top, right, bottom)

#--Exemplo:
canvas.create_oval(200, 0, 300, 100, fill = 'green')



#--Poligono--:

#canvas.create_polygon(x1, y1, x2, y2, x3, y3)

#--Exemplo:

#canvas.create_polygon(0, 0, 100, 200, 300, 50, fill = 'gray')



#--Arca--:

#canvas.create_arc(left, top, right, bottom)

#--Exemplo:

canvas.create_arc(200, 0, 300, 100, fill = 'red', start = 45, extent = 180, style = tk.ARC, outline = 'red', width = 10)
                                                                                    #tk.PIESLICE
                                                                                    #tk.CHORD

#--Texto--:

#canvas.create_text(0,0, text = ' ')

#--Exemplo:
canvas.create_text(100,200, text = 'This is some text', fill = 'green')


#--Mostrar widgets--:

#canvas.create_window(x,y)

#--Exemplo:
canvas.create_window(150,100, window = ttk.Label(window, text = 'text in canvas'))

window.mainloop()