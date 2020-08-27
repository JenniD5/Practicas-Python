
import sys 
sys.path.insert(1,'dsp-modulo') 
from thinkdsp import SinSignal 
from thinkdsp import CosSignal
from thinkdsp import decorate

#modulo para mostrar las graficas 
import matplotlib.pyplot as plt
#dercorate permite ponerle etiquetas 
#crear señal senoidal y asignar propiedades
seno = SinSignal(freq=400, amp=0.7, offset=0)
#offset, fase = en el momento en el que empieza, o sea que este en el segundo 0 pero se comportara como si estuviera en
# el segun tal ya sea se adelante o se atrace. 
#crear grafica
coseno = CosSignal(freq=800, amp=1.1, offset=0)


seno.plot()

#plot permite raficar(frecuenci de muestreo)
decorate(xlabel='tiempo(s) seno', ylabel='Amplitud')
#para mostrar la señal
plt.show()
#el seno comienza en 0 y el coseno en 1, el seno es la componente en x, y el coseno en y
coseno.plot()
decorate(xlabel='tiempo(s) coseno', ylabel='Amplitud')
plt.show()

seno.plot()
coseno.plot()
decorate(xlabel='tiempo(s)', ylabel='Amplitud')
plt.show()
