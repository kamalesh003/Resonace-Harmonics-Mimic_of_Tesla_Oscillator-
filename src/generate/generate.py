import numpy as np
import sounddevice as sd

def generate_sound(frequency, duration, rate, amplitude):
    t = np.linspace(0, duration, int(rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, rate)
    sd.wait()
