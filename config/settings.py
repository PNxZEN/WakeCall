"""Configuration settings for the wake word detection system"""

# Audio settings
CHANNELS = 1
SAMPLE_RATE = 16000
BLOCK_SIZE = 8000

# Model settings
DEFAULT_MODEL_PATH = "models/Baa_buuuuuu.onnx"
DETECTION_THRESHOLD = 0.5

# Logging settings
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO'