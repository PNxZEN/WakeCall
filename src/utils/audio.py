import pyaudio
import wave
import os
import logging

logger = logging.getLogger(__name__)

def play_sound(filename):
    """Play a sound file"""
    try:
        chunk = 1024
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()
    except Exception as e:
        logger.error(f"Error playing sound: {e}")

def validate_audio_device():
    """Validate that audio input device is available and working"""
    try:
        p = pyaudio.PyAudio()
        default_device = p.get_default_input_device_info()
        p.terminate()
        return True, default_device['name']
    except Exception as e:
        logger.error(f"Audio device validation failed: {e}")
        return False, str(e)