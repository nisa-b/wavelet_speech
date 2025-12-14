import matplotlib.pyplot as plt
from scipy.io import wavfile
from utils import downsample
import numpy as np
import pywt
import os

WAVELET = "db4"
TARGET_LEN = 50

def load_and_prepare(path):
    fs, x = wavfile.read(path)
    x = x.astype(float).flatten()
    x50 = downsample(x, TARGET_LEN)
    return x, x50


def plot_group(folder, label):
    files = sorted(os.listdir(folder))

    CA_list = []
    CD_list = []

    for f in files:
        _, x50 = load_and_prepare(os.path.join(folder, f))
        cA, cD = pywt.dwt(x50, WAVELET)
        CA_list.append(cA)
        CD_list.append(cD)

    CA = np.array(CA_list).T   # (25, n_ses)
    CD = np.array(CD_list).T

    # ===============================
    # GÖRSELLEŞTİRME
    # ===============================

    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)
    plt.imshow(CA, aspect="auto", cmap="viridis")
    plt.colorbar()
    plt.title(f"{label} – CA (Yaklaşım Katsayıları)")
    plt.xlabel("Ses indexi")
    plt.ylabel("Katsayı indexi")

    plt.subplot(1,2,2)
    plt.imshow(CD, aspect="auto", cmap="viridis")
    plt.colorbar()
    plt.title(f"{label} – CD (Detay Katsayıları)")
    plt.xlabel("Ses indexi")
    plt.ylabel("Katsayı indexi")

    plt.tight_layout()
    plt.show()


# ===============================
# EVET ve HAYIR grupları
# ===============================

plot_group("data/evet", "EVET")
plot_group("data/hayir", "HAYIR")
