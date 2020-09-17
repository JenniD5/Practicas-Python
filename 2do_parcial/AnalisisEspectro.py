import sys
sys.path.insert(1,'dsp-modulo')
from thinkdsp import SinSignal 
from thinkdsp import decorate
import thinkplot 

frecuencia1 = SinSignal(freq=1500, amp=0.3, offset=0)
freuencia2 = SinSignal(freq=380, amp=0.6, offset=0)
resultante1 = frecuencia1 + freuencia2
wave_resultante1 = resultante1.make_wave(duration=1, start=0, framerate=44100)
frecuencia3= SinSignal(freq=5300, amp= 1.0, offset= 0)
frecuencia4 = SinSignal(freq=12300, amp=0.1, offset=0)
resultante2 = frecuencia3 + frecuencia4
wave_resultante2 = resultante2.make_wave(duration=6, start=1.3, framerate=44100)
waveResultantes = wave_resultante1 + wave_resultante2

waveResultantes.plot()
decorate(xlabel="tiempo(s)")
thinkplot.show()

#graficacion de espectro
espectro = waveResultantes.make_spectrum()
espectro.plot()
decorate(xlabel="frecuencia(hz)")
thinkplot.show()