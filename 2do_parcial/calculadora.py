from tkinter import*
ventana =Tk()
ventana.title("calculadora de propinas")
ventana.geometry("400x400")


strTotal = StringVar()
strTotal.set("$0.00")
#funciones
def calcular():
    #conseguir lo que introdujo el usuario, pero como lo trae como string, hay que ponerle float
    total = float(txtCuenta.get()) + float(txtCuenta.get()) * (float(sclPropina.get()/100))
    strTotal.set("$" + str(total))
    





lblCuenta = Label(ventana, text="cuenta: ")
lblCuenta.pack()

txtCuenta = Entry(ventana)
txtCuenta.pack()

lblPorcentajePropina = Label(ventana, text="porcentaje de propina")
lblPorcentajePropina.pack()

sclPropina = Scale(ventana, from_=0, to_=20, orient=HORIZONTAL)
sclPropina.pack()

btnCalcular = Button(ventana, text="calcular", command=calcular)
btnCalcular.pack()

lblTotal = Label(ventana, text="Total a pagar: ")
lblTotal.pack()

lblMontoTotal = Label(ventana, textvariable=strTotal)
lblMontoTotal.pack()

ventana.mainloop()