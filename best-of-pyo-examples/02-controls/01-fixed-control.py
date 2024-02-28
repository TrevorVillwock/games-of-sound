"""
01-fixed-control.py - Number as argument.

Audio objects behaviour can be controlled by passing
value to their arguments at initialization time.

"""
from pyo import *

s = Server().boot()
s.amp = 0.1

# Sets fundamental frequency
freq = 200

# Approximates a sqaure waveform by adding odd harmonics with
# amplitude proportional to the inverse of the harmonic number.
# mul = amplitude
sh1 = Sine(freq=freq, mul=1).out()
sh2 = Sine(freq=freq * 3, mul=1.0 / 3).out()
sh3 = Sine(freq=freq * 5, mul=1.0 / 5).out()
sh4 = Sine(freq=freq * 7, mul=1.0 / 7).out()
sh5 = Sine(freq=freq * 9, mul=1.0 / 9).out()
sh6 = Sine(freq=freq * 11, mul=1.0 / 11).out()

square = sh1 + sh1 + sh2 + sh3 + sh4 + sh5 + sh6

# Approximates a sqaure waveform by adding odd harmonics with
# amplitude proportional to the inverse of the harmonic number.
# mul = amplitude
sqh1 = Sine(freq=freq, mul=1).out()
sqh2 = Sine(freq=freq * 3, mul=1.0 / 3).out()
sqh3 = Sine(freq=freq * 5, mul=1.0 / 5).out()
sqh4 = Sine(freq=freq * 7, mul=1.0 / 7).out()
sqh5 = Sine(freq=freq * 9, mul=1.0 / 9).out()
sqh6 = Sine(freq=freq * 11, mul=1.0 / 11).out()

square = sqh1 + sqh2 + sqh3 + sqh4 + sqh5 + sqh6

# Approximates a triangle waveform by adding odd harmonics with
# amplitude proportional to the inverse square of the harmonic number.
th1 = Sine(freq=freq, mul=1).out()
th2 = Sine(freq=freq * 3, phase=0.5, mul=1.0 / pow(3, 2)).out()
th3 = Sine(freq=freq * 5, mul=1.0 / pow(5, 2)).out()
th4 = Sine(freq=freq * 7, phase=0.5, mul=1.0 / pow(7, 2)).out()
th5 = Sine(freq=freq * 9, mul=1.0 / pow(9, 2)).out()
th6 = Sine(freq=freq * 11, phase=0.5, mul=1.0 / pow(11, 2)).out()

tri = th1 + th2 + th3 + th4 + th5 + th6

# Displays the final waveform
sp = Scope(tri)
# sp = Scope(h1 * h2 * h3 * h4 * h5 * h6)

s.gui(locals())
