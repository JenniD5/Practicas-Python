import sys 
sys.path.insert(1,'dsp-modulo') 
from thinkdsp import SinSignal 
from thinkdsp import read_wave
from thinkdsp import decorate

import matplotlib.pyplot as plt

sonido = SinSignal(freq=440, amp=1, offset=0)
wave_sonido = sonido.make_wave(duration=1.0, start=0, framerate=44100)
#3 caracteristicas principales;duration, comienzo y frecuencia de muestreo

decorate(xlabel="tiempo(s)", ylabel="Amplitud")
#wave_sonido.plot()
#plt.show()
wave_sonido.write("sonido_original.wav")
print(type(wave_sonido), "inicio: " + str(wave_sonido.start), " duracion: "+ str(wave_sonido.duration), " frecuencia de muestro: " + str(wave_sonido.framerate))
#la frecuencia de muestro en un valor modificable
wave_sonido.framerate = wave_sonido.framerate/2
wave_sonido.write("sonido_modificado.wav")
print("nueva frecuencia de muestreo: " + str(wave_sonido.framerate))

decorate(xlabel="tiempo(s)", ylabel="Amplitud")
#wave_sonido.plot()
#plt.show()

#thinkdsp toma en cuenta el inicio y la duracion, y todas las muestras que encuentre las va a graficar en ese tiempo, no toma en cuenta la frecuencia de muestreo a la hora de gaficar para el tiempo 
#si dura 1s todas las muestras las va a dividir en ese segundo
#graficamente no se vería el resultad, se veria si se representará como un sonido 
#el wave siempre va a empezar en cero, dandole priorida dal numero de muestras. 

campana = read_wave("dsp-recursos/18871__zippi1__sound-bell-440hz.wav")
segmento_campana = campana.segment(8,1)


plt.title("Campana_segmento")
decorate(xlabel="tiempo(s)", ylabel="Amplitud")
segmento_campana.plot()
plt.show()
segmento_campana.write("campana_original.wav")
segmento_campana.framerate = segmento_campana.framerate/2
segmento_campana.write("campana_modificada.wav")
