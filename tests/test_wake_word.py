# Basic test cases for the wake word detector
import unittest
import os
from src.detect_wake_word import WakeWordDetector
from src.utils.audio import validate_audio_device

class TestWakeWordDetector(unittest.TestCase):
    def setUp(self):
        self.detector = WakeWordDetector()

    def test_model_loading(self):
        """Test if the wake word model loads successfully"""
        self.assertIsNotNone(self.detector.oww_model)

    def test_audio_device(self):
        """Test if audio device is available and working"""
        status, device_name = validate_audio_device()
        self.assertTrue(status)
        self.assertIsNotNone(device_name)

if __name__ == '__main__':
    unittest.main()