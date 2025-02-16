# Voice-Activated Call Notification System

A practical solution for improving home communication using AI-powered wake word detection. This system listens for a specific wake word ("baabu") and triggers an automated phone call notification using Twilio's API.

## The Problem It Solves
Living in a multi-story home created communication challenges - particularly when family members couldn't hear each other calling from different floors. This project provides an automated solution that ensures important calls for attention aren't missed.

## Key Features

- Custom wake word detection using OpenWakeWord ML models
- Real-time audio processing from microphone input
- Automated phone call notifications via Twilio
- Support for both ONNX and TFLite model formats
- Low latency response time
- Configurable detection sensitivity

## Technical Skills Demonstrated

- **Machine Learning**
  - Custom wake word model training
  - Audio signal processing
  - Model optimization and conversion (ONNX/TFLite)

- **Software Engineering**
  - Clean code architecture and modularity
  - Environment configuration management
  - API integration (Twilio)
  - Real-time audio processing

- **Best Practices**
  - Secure credential management
  - Configuration externalization
  - Comprehensive documentation
  - Error handling and logging

## Prerequisites

- Python 3.8+
- Required packages (see `requirements.txt`)
- Twilio account for notification feature

## Installation

1. Clone this repository
```bash
git clone <your-repo-url>
cd voice-activated-notification
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment
   - Copy `.env.template` to `.env`
   - Add your Twilio credentials and phone numbers

## Usage

1. Start the wake word detection:
```bash
python src/detect_wake_word.py
```

2. When the wake word is detected, the system will automatically:
   - Recognize the custom wake word ("baabu")
   - Initiate a phone call via Twilio
   - Connect the caller to the recipient

## Project Structure

```
├── src/                    # Source code
│   ├── detect_wake_word.py # Main detection script
│   ├── notification.py     # Twilio integration
│   └── utils/             # Helper utilities
├── models/                 # Trained wake word models
├── config/                 # Configuration files
├── docs/                   # Documentation
└── tests/                 # Test suite
```

## Model Training

The wake word model was trained using OpenWakeWord's framework. See `/docs/training.md` for details on:
- Data collection process
- Training parameters
- Model performance metrics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms found in the LICENSE file.

## Acknowledgments

- Built on [OpenWakeWord](https://github.com/dscripka/openWakeWord)
- Uses Twilio for notifications