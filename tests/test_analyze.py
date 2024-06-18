import unittest
import numpy as np
from src.analyze.analyze import analyze_sound

class TestAnalyzeSound(unittest.TestCase):
    def test_analyze_sound(self):
        rate = 44100
        duration = 1.0
        t = np.linspace(0, duration, int(rate * duration), endpoint=False)
        signal = 0.5 * np.sin(2 * np.pi * 440 * t)
        dominant_frequency = analyze_sound(signal, rate)
        self.assertAlmostEqual(dominant_frequency, 440, places=0)

if __name__ == '__main__':
    unittest.main()
