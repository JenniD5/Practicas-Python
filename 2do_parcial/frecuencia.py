import sys
sys.path.insert(1,'dsp-modulo')
from thinkdsp import SinSignal
from thinkdsp import decorate
import thinkplot 

senalUno = SinSignal(freq=380, amp=0.8, offset=0)
senalDos = SinSignal(freq=200, amp=0.5, offset=0)
mezcla = senalUno + senalDos
waveMezcla = mezcla.make_wave(duration=2, start=0, framerate=44100)
decorate(xlabel="tiempo(s)")
waveMezcla.plot()
thinkplot.show()

espectro = waveMezcla.make_spectrum()
espectro.plot()
decorate(xlabel="frecuencia (Hz)")
thinkplot.show()
#frecuencia=lugar el en eje x
#amplitud = eje y