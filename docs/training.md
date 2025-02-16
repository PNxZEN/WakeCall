# Wake Word Model Training Documentation

This document details the process of training the custom wake word model for the word "baabu" using OpenWakeWord.

## Data Collection Process

The wake word model was trained using:
- 50+ positive samples of the wake word "baabu"
- Recorded in different:
  - Voice tones
  - Room acoustics
  - Distances from microphone
  - Background noise conditions

## Training Parameters

```python
# Key training parameters used
{
    "epochs": 100,
    "batch_size": 32,
    "learning_rate": 0.001,
    "validation_split": 0.2,
    "audio_length": 1.5  # seconds
}
```

## Model Performance

- False Acceptance Rate (FAR): < 0.1%
- False Rejection Rate (FRR): < 5%
- Response Time: < 1 second
- Model Size: ~4MB (ONNX format)

## Model Optimization

The model was optimized using:
1. ONNX Runtime optimization
2. TFLite conversion for edge deployment
3. Quantization to reduce model size

## Testing Methodology

The model was tested against:
- Different speakers
- Various background noise conditions
- Different room acoustics
- Multiple wake word variations

## Future Improvements

1. Implement dynamic noise adaptation
2. Add support for multiple wake words
3. Reduce model latency further
4. Implement voice authentication