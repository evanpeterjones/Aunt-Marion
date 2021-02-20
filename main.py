'''
import wave, struct, math, random
from struct import pack
from math import pi, sin

sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz
obj = wave.open('sound.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(99999):
   value = (i % 0x7fff)
   data = struct.pack('<h', value)
   obj.writeframesraw( data )
obj.close()

def sound_generation(name, freq, dur, vol):
    a = open(name, 'wb')
    a.write(pack('>4s5L', '.snd'.encode("utf-8"), 24, 2*dur, 2, 9000, 1))
    sine_factor = 2 * pi * freq/8000
    for seg in range(8*dur):
        sine_segments = sin(seg * sine_factor)
        val = pack('b', int(vol * sine_segments))
        a.write(val)
    a.close()

sound_generation("test.wav", 440, 1, 1)
'''
import numpy as np
import wavio

# Parameters
rate = 44100    # samples per second
T = 3           # sample duration (seconds)
f = 440.0       # sound frequency (Hz)

# Compute waveform samples
t = np.linspace(0, T, T*rate, endpoint=False)
x = np.sin(2*np.pi * f * t)

# Write the samples to a file
wavio.write("sine.wav", x, rate, sampwidth=3)
