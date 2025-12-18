import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os

fs = 16000 # Sampling Rate (Örnekleme Hızı)
duration = 1.0 # Kayıt suresi (1 sn)

def record(label, count):
    print(f"{label.upper()} söyle ({count})...")
    audio = sd.rec(int(fs * duration), samplerate=fs, channels=1)
    sd.wait()

    filename = f"data/{label}/{label}_{count:02d}.wav"
    wav.write(filename, fs, audio)
    print("Kaydedildi:", filename)

os.makedirs("data/evet", exist_ok=True)
os.makedirs("data/hayir", exist_ok=True)

n = int(input("Her kelimeden kaç kayıt alınacak? "))

for i in range(1, n+1):
    input("\nENTER'a bas → EVET")
    record("evet", i)

for i in range(1, n+1):
    input("\nENTER'a bas → HAYIR")
    record("hayir", i)

