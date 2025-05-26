import os
import queue
import sounddevice as sd
import vosk
import json

# Path to the Russian model
model_path = "vosk-model-small-ru-0.22"


# Initialize the model
if not os.path.exists(model_path):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

print(sd.query_devices())
# exit(1)

model = vosk.Model(model_path)
samplerate = 16000
q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status)
    q.put(bytes(indata))

# Start the audio stream
device_index=1
with sd.InputStream(samplerate=samplerate, channels=1, callback=callback, device=device_index):
    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = rec.Result()
            print(json.loads(result)["text"])
        else:
            print(rec.PartialResult())