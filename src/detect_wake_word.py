import logging
import os
import sys
import sounddevice as sd
import numpy as np
from openwakeword import Model
from notification import send_notification

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WakeWordDetector:
    def __init__(self, model_path="models/Baa_buuuuuu.onnx", threshold=0.5):
        self.threshold = threshold
        try:
            self.oww_model = Model(wakeword_models=[model_path])
            logger.info("Wake word model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load wake word model: {e}")
            sys.exit(1)

    def audio_callback(self, indata, frames, time, status):
        """Callback for processing audio chunks"""
        if status:
            logger.warning(f"Audio callback status: {status}")
            return
        
        try:
            # Process audio frame
            prediction = self.oww_model.predict(indata)
            
            # Check if wake word detected
            if prediction[0] > self.threshold:
                logger.info("Wake word detected!")
                send_notification()
        except Exception as e:
            logger.error(f"Error processing audio: {e}")

    def start_listening(self):
        """Start listening for wake word"""
        try:
            with sd.InputStream(
                channels=1,
                samplerate=16000,
                blocksize=8000,
                callback=self.audio_callback
            ):
                logger.info("Started listening for wake word...")
                while True:
                    sd.sleep(1000)
        except KeyboardInterrupt:
            logger.info("Stopping wake word detection...")
        except Exception as e:
            logger.error(f"Error in audio stream: {e}")

if __name__ == "__main__":
    detector = WakeWordDetector()
    detector.start_listening()