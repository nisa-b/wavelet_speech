import matplotlib.pyplot as plt
from scipy.io import wavfile
from utils import downsample
import numpy as np
import pywt

WAVELET = "db4"
TARGET_LEN = 50

def wavelet_energy(c):
    return np.sum(c ** 2)

def plot_signal(path, label):
    fs, x = wavfile.read(path)
    x = x.astype(float).flatten()
    x50 = downsample(x, TARGET_LEN)

    cA, cD = pywt.dwt(x50, WAVELET)

    plt.figure(figsize=(10,6))

    # -------------------------
    # 1️⃣ Ham sinyal
    # -------------------------
    plt.subplot(3,1,1)
    plt.plot(x)
    plt.title(f"{label} – Ham Sinyal (Zaman Alanı)")
    plt.ylabel("Genlik")

    # -------------------------
    # 2️⃣ CA
    # -------------------------
    plt.subplot(3,1,2)
    plt.stem(cA)
    plt.title(f"{label} – Yaklaşım Katsayıları (CA)")
    plt.ylabel("Genlik")

    # -------------------------
    # 3️⃣ CD
    # -------------------------
    plt.subplot(3,1,3)
    plt.stem(cD)
    plt.axhline(0, color="red")
    plt.title(f"{label} – Detay Katsayıları (CD)")
    plt.xlabel("Katsayı indeksi")
    plt.ylabel("Genlik")

    plt.tight_layout()
    plt.show()

    E_CA = wavelet_energy(cA)
    E_CD = wavelet_energy(cD)

    print(f"{label} için enerji:")
    print(f"  CA enerjisi = {E_CA:.4f}")
    print(f"  CD enerjisi = {E_CD:.4f}")
    print(f"  CD / CA oranı = {E_CD / E_CA:.4f}")




# ===============================
# EVET ve HAYIR AYRI AYRI
# ===============================

plot_signal("data/evet/evet_01.wav", "EVET")
plot_signal("data/hayir/hayir_01.wav", "HAYIR")
