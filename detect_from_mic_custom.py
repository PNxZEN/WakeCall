# Copyright 2022 David Scripka. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Imports
import pyaudio
import numpy as np
from openwakeword.model import Model
import twilio_use
from threading import Thread
# import argparse

# # Parse input arguments
# parser=argparse.ArgumentParser()
# parser.add_argument(
#     "--chunk_size",
#     help="How much audio (in number of samples) to predict on at once",
#     type=int,
#     default=1280,
#     required=False
# )
# parser.add_argument(
#     "--model_path",
#     help="The path of a specific model to load",
#     type=str,
#     default="",
#     required=False
# )
# parser.add_argument(
#     "--inference_framework",
#     help="The inference framework to use (either 'onnx' or 'tflite'",
#     type=str,
#     default='tflite',
#     required=False
# )

# args=parser.parse_args()

# # **Modified Section: Argument Parsing**
# # Instead of parsing command-line arguments, set the values directly since we are in a notebook environment.
# args = argparse.Namespace(
#     chunk_size=1280,
#     model_path=r"D:\PNS\Py\OpenWakeWord\Baabuu.onnx",
#     inference_framework='onnx'
# )

# Get microphone stream
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
# CHUNK = args.chunk_size
CHUNK= 1280
audio = pyaudio.PyAudio()
mic_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

t = Thread(target= twilio_use.call)
def start_call():
    try:
        if not t.is_alive():
            t.start()
    except:
        return

# Load pre-trained openwakeword models
# if args.model_path != "":
#     owwModel = Model(wakeword_models=[args.model_path], inference_framework=args.inference_framework)
# else:
#     owwModel = Model(inference_framework=args.inference_framework)

owwModel= Model(wakeword_models= ['Baa_buuuuuu.onnx'], inference_framework= 'onnx')
n_models = len(owwModel.models.keys())

global num_detects
num_detects= 0

# Run capture loop continuosly, checking for wakewords
if __name__ == "__main__":
    # Generate output string header
    print("\n\n")
    print("#"*100)
    print("Listening for wakewords...")
    print("#"*100)
    print("\n"*(n_models*3))

    while True:
        # Get audio
        audio = np.frombuffer(mic_stream.read(CHUNK), dtype=np.int16)

        # Feed to openWakeWord model
        prediction = owwModel.predict(audio)

        # Column titles
        n_spaces = 16
        output_string_header = """
            Model Name         | Score | Wakeword Status
            --------------------------------------
            """

        for mdl in owwModel.prediction_buffer.keys():
            # Add scores in formatted table
            scores = list(owwModel.prediction_buffer[mdl])
            curr_score = format(scores[-1], '.20f').replace("-", "")

            output_string_header += f"""{mdl}{" "*(n_spaces - len(mdl))}   | {curr_score[0:5]} | {"--"+" "*20 if scores[-1] <= 0.01 else "Wakeword Detected!"}
            """
                    
        if scores[-1]<= 0.5:
            num_detects+= 1
            if num_detects == 2:
                num_detects= 0
                start_call()
                print("Calling...")

        # Print results table
        print("\033[F"*(4*n_models+1))
        print(output_string_header, "                             ", end='\r')