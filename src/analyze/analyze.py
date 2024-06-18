from scipy.fft import fft, fftfreq
import numpy as np


def analyze_sound(signal, rate):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / rate)
    idx = np.argmax(np.abs(yf))
    dominant_frequency = abs(xf[idx])
    return dominant_frequency
