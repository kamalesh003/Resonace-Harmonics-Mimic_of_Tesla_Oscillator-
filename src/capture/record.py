import pyaudio
import numpy as np

def record_sound(duration, rate):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=1024)
    frames = []
    for _ in range(0, int(rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(np.frombuffer(data, dtype=np.int16))
    stream.stop_stream()
    stream.close()
    p.terminate()
    return np.hstack(frames)
