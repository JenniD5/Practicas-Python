import sys 
sys.path.insert(1,'dsp-modulo')
from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave

import thinkplot 
import matplotlib.pyplot as plt

wavetelefono = read_wave("telefono.wav")
wavetelefono.plot()
plt.title("Todos los digitos")
decorate(xlabel="tiempo(s)")
thinkplot.show()

#espectro = wavetelefono.make_spectrum()
#espectro.plot()
#decorate(xlabel="frecuencia(hz)")

#thinkplot.show()

wavePrimerDigito = wavetelefono.segment(start=0, duration=0.5)
#wavePrimerDigito.plot()
#decorate(xlabel="tiempo(s)")
#thinkplot.show()

espectroPrimerDigito = wavePrimerDigito.make_spectrum()
espectroPrimerDigito.plot()
plt.title("Primer Digito")
decorate(xlabel="frecuencia(hz)")
thinkplot.show()

waveSegundoDigito = wavetelefono.segment(start=0.5, duration=0.5)
espectroSegundoDigito = waveSegundoDigito.make_spectrum()
espectroSegundoDigito.plot()
plt.title("Segundo digito")
decorate(xlabel="frecuencia(hz)")
thinkplot.show()

#telefono: 22-4

waveTercerDigito = wavetelefono.segment(start=1, duration=0.5)
espectroTercerDigito = waveTercerDigito.make_spectrum()
espectroTercerDigito.plot()
plt.title("Tercer digito")
decorate(xlabel="frecuencia(hz)")
thinkplot.show()

wave4Digito = wavetelefono.segment(start=1.5, duration=0.5)
espectro4Digito = wave4Digito.make_spectrum()
espectro4Digito.plot()
plt.title("Cuarto digito")
decorate(xlabel="frecuencia4(hz)")
thinkplot.show()

wave5Digito = wavetelefono.segment(start=2, duration=0.5)
espectro5Digito = wave5Digito.make_spectrum()
espectro5Digito.plot()
plt.title("Quinto digito")
decorate(xlabel="frecuencia5(hz)")
thinkplot.show()


wave6Digito = wavetelefono.segment(start=2.5, duration=0.5)
espectro6Digito = wave6Digito.make_spectrum()
espectro6Digito.plot()
plt.title("Sexto digito")
decorate(xlabel="frecuencia6(hz)")
thinkplot.show()