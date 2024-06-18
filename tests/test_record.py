import unittest
from src.capture.record import record_sound

class TestRecordSound(unittest.TestCase):
    def test_record_sound(self):
        duration = 1.0
        rate = 44100
        sound = record_sound(duration, rate)
        self.assertEqual(len(sound), int(rate * duration))

if __name__ == '__main__':
    unittest.main()
