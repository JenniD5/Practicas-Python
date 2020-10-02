from tkinter import *

ventana = Tk()
ventana.title("Mi ventana")
#tamaño
ventana.geometry("800x600")

etiqueta = Label(ventana, text="esto es una etiqueta")
#para agregar a la ventana
etiqueta.pack()

segundaetiqueta = Label(ventana, text="segunda etiqueta")
segundaetiqueta.pack()
#ingreso de texto
ingresoTexto = Entry(ventana)
ingresoTexto.pack()
#boton
boton = Button(ventana, text="mi boton")
boton.pack()
#ejecutar ventana
ventana.mainloop()

