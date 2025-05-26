# import os
# import queue
# import sounddevice as sd
# import vosk
# import json

import pyaudio
import json
from vosk import Model, KaldiRecognizer, SetLogLevel

# # Path to the Russian model
# model_path = "vosk-model-ru-0.22" # big model
model_path = "vosk-model-small-ru-0.22"

# Отключение логов Vosk для чистого вывода
SetLogLevel(-1)

# https://alphacephei.com/vosk/models

try:
    model = Model(model_path)
except Exception as e:
    print(f"Ошибка при загрузке модели Vosk: {e}")
    print(f"Убедитесь, что модель скачана и распакована в '{model_path}'")
    exit()

samplerate = 16000 # Частота дискретизации (стандарт для моделей Vosk)
recognizer = KaldiRecognizer(model, samplerate)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=samplerate,
                input=True,
                frames_per_buffer=512) # Размер буфера, может быть настроен

print("Tell something (press Ctrl+C to exit)")

try:
    stream.start_stream()
    while True:
        data = stream.read(1024, exception_on_overflow=False) # Читаем данные из микрофона
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            if result['text']:
                print(f"You told: {result['text']}")
        else:
            # Для частичных результатов (пока вы говорите)
            # partial_result = json.loads(recognizer.PartialResult())
            # if partial_result['partial']:
            #     print(f"Partial result: {partial_result['partial']}", end='\r')
            pass

except KeyboardInterrupt:
    print("\nStop listening.")
except Exception as e:
    print(f"Error occured: {e}")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Mic closed")