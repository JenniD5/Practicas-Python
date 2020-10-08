from tkinter import*
from tkinter.filedialog import askopenfilename #abrir el cuadro de dialogo 

#graficos dentro de un interfaz 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


import sys 
sys.path.insert(1,'dsp-modulo')
from thinkdsp import read_wave
import numpy




principal = Tk()
principal.title("Analisis audio")
principal.geometry("400x400")
principal.configure(bg='pink')

strDireccionArchivo = StringVar()
strDireccionArchivo.set("Dirección del contenido")

strsecuenciaNumeros=StringVar()
strsecuenciaNumeros.set("Numero contenido en el audio")

def abrirArchivo():
    direccionArchivo=askopenfilename()
    strDireccionArchivo.set(direccionArchivo)

    #analisis del audio 

    telefono = ""
    #poner direccion del telefono 
    waveTelefono = read_wave(direccionArchivo)
    #arreglo
    segmentosNumero = []
    for i in range(6):
        segmentosNumero.append(waveTelefono.segment(start=i*0.5, duration=0.5))
        
        


    #hs dentro de los espectros, amplitud espetral(y)
    #fs: frecuencias (x)
    #hs[50000] fs[50000], daria hs y fs del indice 50000
    '''espectro = segmentosNumero[0].make_spectrum()
    espectro.plot()
    thinkplot.show()'''

    frecuenciasBajasDTMF = [697,770,853,941]
    frecuenciasAltasDTMF = [1209,1336,1477]
    #cuantos Hz mas o menos se pueden tolerar para identificar una frecuencia 
    tolerancia = 10

    for segmento in segmentosNumero:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes=[]
        i=0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500: #guarda los picos mayores de 500 en y 
                #se va al eje x para ver que representa esa amplitud 
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1 
        frecuenciaBaja = 0
        frecuenciaAlta = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciasBajasDTMF:
                #comparar frecuencia con frecuenciaDTMF
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    frecuenciaBaja = frecuenciaDTMF
            for frecuenciaDTMF in frecuenciasAltasDTMF:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    frecuenciaAlta = frecuenciaDTMF
        if frecuenciaAlta == 1209:
            if frecuenciaBaja == 697:
                telefono = telefono + "1"
            elif frecuenciaBaja == 770:
                telefono = telefono + "4"
            elif frecuenciaBaja == 852:
                telefono = telefono + "7"
            elif frecuenciaBaja == 941:
                telefono = telefono + "*"
            else: 
                telefono = telefono + "X"

        elif frecuenciaAlta == 1336:
            if frecuenciaBaja == 697:
                telefono = telefono + "2"
            elif frecuenciaBaja == 770:
                telefono = telefono + "5"
            elif frecuenciaBaja == 852:
                telefono = telefono + "8"
            elif frecuenciaBaja == 941:
                telefono = telefono + "0"
            else: 
                telefono = telefono + "X"

        elif frecuenciaAlta == 1477:
            if frecuenciaBaja == 697:
                telefono = telefono + "3"
            elif frecuenciaBaja == 770:
                telefono = telefono + "6"
            elif frecuenciaBaja == 852:
                telefono = telefono + "9"
            elif frecuenciaBaja == 941:
                telefono = telefono + "#"
            else: 
                telefono = telefono + "X"
        else:
            telefono = telefono +"X"

    strsecuenciaNumeros.set(telefono)

    #contedor de lagrafica
    figure = Figure(figsize=(5,3), dpi=100)
    #meterle la grafica, siempre 111, xyz, que se va a graficar en el ejex, y en el eje y
    figure.add_subplot(111).plot(waveTelefono.ts, waveTelefono.ys)
    #para los waves, eje x=ts, eje y=ys

    #añadir a ventana
    canvas=FigureCanvasTkAgg(figure, master=principal)
    canvas.draw()
    #mostrar en la ventana
    canvas.get_tk_widget().pack()

btnAbrir = Button(principal, text="abrir archivo wav", command=abrirArchivo)
btnAbrir.configure(bg='violet')
btnAbrir.pack()

lblArchivo = Label(principal, textvariable=strDireccionArchivo)
lblArchivo.configure(bg = 'violet')
lblArchivo.pack()

lblSecuenciaNumeros= Label(principal, textvariable=strsecuenciaNumeros)
lblSecuenciaNumeros.configure(bg = 'violet')
lblSecuenciaNumeros.pack()
mainloop()


