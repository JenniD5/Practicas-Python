#tambien conocido como ruido rojo 

import sys
sys.path.insert(1,'dsp-modulo')
import numpy as np
import thinkplot as plt 

from thinkdsp import decorate 
from thinkdsp import BrownianNoise

#para que tenga la misma secuencia 
np.random.seed(17)

señal = BrownianNoise()
wave_señal=señal.make_wave(duration=0.5, framerate=22050)
#wave_señal.write("ruido_browniano.wav")
#no suena tan brilloso; no tiene tantas frecuencias altas, no hay tanto escandala como en el ruido blanco 
wave_señal.plot()
decorate(xlabel="tiempo", ylabel="amplitud")
plt.show()

espectro = wave_señal.make_spectrum()
espectro.plot_power()

#graficar de manera logaritmica
loglog=dict(xscale="log", yscale="log")
decorate(xlabel="frecuencia", ylabel="power", **loglog)
plt.show()

#el ruido blanco tiene presencia de la mayoria de las frecuencias 
#si se estimaba la pendiente del esprectro, tiende a cero

pendiente = espectro.estimate_slope()
print("pendiente:" + str(pendiente.slope))
#ruido rojo: sus espectros se comportan de manera muy parecida 
#la pendiente con numeros muy cercanos a 2, + o -

#cualquier pendiende, o ruido que tenga la pendiente entre cero y dos, se denomina ruido rosa 





