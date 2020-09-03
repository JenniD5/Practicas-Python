import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal 
from thinkdsp import decorate

from thinkdsp import read_wave #leer
from thinkdsp import play_wave #reproducir

import matplotlib.pyplot as plt

seno = SinSignal(freq=19940, amp=1, offset=0)
segundo_seno = SinSignal(freq=340, amp=0.7, offset=0)
tercer_seno = SinSignal(freq=600, amp=0.4, offset=0)

wave_seno = seno.make_wave(duration=1.0, start=0, framerate=44100)
#wake para cear una onda o para leer algun archivo de audio 
wave_segundo_seno = segundo_seno.make_wave(duration=1.0, start=1, framerate=44100)
wave_tercer_seno = tercer_seno.make_wave(duration=1.0, start=2, framerate=44100)

resulante = wave_seno + wave_segundo_seno + wave_tercer_seno

decorate(xlabel="tiempo(s)", ylabel="amplitud")
resulante.plot()
resulante.write("sonido_resultante1.wav")
plt.show()
#señal senoidal en distintos medios 
