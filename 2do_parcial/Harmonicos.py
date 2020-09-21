import sys
sys.path.insert(1,'dsp-modulo') 

from thinkdsp import SinSignal
from thinkdsp import SquareSignal
from thinkdsp import decorate

import matplotlib.pyplot as plt
import thinkplot
import numpy

senalRectangular = SquareSignal(freq=2, amp=1.0, offset=numpy.pi)
wave_senalRec = senalRectangular.make_wave(duration=1, start=0, framerate=44100)

#SEÑAL SENOIDAL 
senalSenoidal = SinSignal(freq=2, amp=1.0, offset=0)
waveSenoidal = senalSenoidal.make_wave(duration=1, start=0, framerate=44100)

harmonico1 = SinSignal(freq=senalSenoidal.freq*3, amp=0.3, offset=0)
harmonico2 = SinSignal(freq=senalSenoidal.freq*5, amp=0.25, offset=0)
harmonico3 = SinSignal(freq=senalSenoidal.freq*7, amp=0.2, offset=0)
harmonico4 = SinSignal(freq=senalSenoidal.freq*9, amp=0.15, offset=0)
harmonico5 = SinSignal(freq=senalSenoidal.freq*11, amp=0.1, offset=0)
harmonico6 = SinSignal(freq=senalSenoidal.freq*12, amp=0.05, offset=0)
mezcla = senalSenoidal + harmonico1 + harmonico2 + harmonico3 + harmonico4 + harmonico5 + harmonico6
waveMezcla = mezcla.make_wave(duration=1, start=0, framerate=44100)

wave_senalRec.plot()
waveMezcla.plot()
plt.title("señales rectangulares ")
decorate(xlabel= "tiempo (s)")
thinkplot.show()

espectroRec = wave_senalRec.make_spectrum()
espectroSeno = waveMezcla.make_spectrum()
espectroRec.plot()
espectroSeno.plot()
plt.title("espectros de señales rectangulares ")
decorate(xlabel= "frecuencia (Hz)")
thinkplot.show()

#la presencia de frecuencias en la Rectangular, no quiere decir que infiera, 
#sino que ayuda a darle esa forma
#esos son los harmonicos 

