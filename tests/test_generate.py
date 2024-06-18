import unittest
from src.generate.generate import generate_sound

class TestGenerateSound(unittest.TestCase):
    def test_generate_sound(self):
        # This test is more of a placeholder since sound generation is hard to test without listening
        duration = 1.0
        rate = 44100
        frequency = 440
        amplitude = 0.5
        try:
            generate_sound(frequency, duration, rate, amplitude)
        except Exception as e:
            self.fail(f"generate_sound raised Exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()
