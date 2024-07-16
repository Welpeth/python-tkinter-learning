import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)


#|--------------- Opções Janela ------------------|
#Criar janela
window = ttk.Window(themename = 'darkly')

#Titulo da janela
window.title('Demo')

#Tamanho da Janela
window.geometry('300x150')

#|--------------- Titulo ------------------| 

#Criar titulo
titulo_label = ttk.Label(master = window, text = 'Milhas para quilômetros', font = 'Montserrat 15 bold')

#Rodar o titulo na janela
titulo_label.pack()

#|--------------- Botões e Campos de Digitar ------------------| 
#Criar o Campo para colocar os botões e campo de digitar
input_frame = ttk.Frame(master = window)

#Criar botão
button = ttk.Button(master = input_frame, text = 'Converter', command = convert)

#Criar variavel para armazenar o que vai ser digitado
entry_int = tk.IntVar()

#Criar campo de digitar
entry = ttk.Entry(master = input_frame, textvariable = entry_int)


entry.pack(side = 'left', padx = 5)
button.pack(side = 'left', padx = 5)
input_frame.pack(pady = 15)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Montserrat 10', textvariable = output_string)
output_label.pack(pady = 15)

#Rodar a Janela
window.mainloop()