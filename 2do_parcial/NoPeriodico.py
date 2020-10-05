import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import Chirp
from thinkdsp import read_wave

import thinkplot
import matplotlib.pyplot as plt


#senal = Chirp(start=220, end=440, amp=1)
#wavesenal = senal.make_wave(duration=1, framerate=11025)
wave=read_wave("telefono1.wav")

espectro = wave.make_spectrum()
#seg_length=cantidad de muestras en y,relacion muestras por segundo, eje y=rango de frecuencias contidas dividido en 512
espectrograma = wave.make_spectrogram(seg_length=1024)
plt.title("Chirp")
wave.plot()
thinkplot.show()

plt.title("Chirp espcerto")
espectro.plot()
thinkplot.show()

espectrograma.plot()
thinkplot.show()

