import os
import numpy as np
from scipy.io import wavfile
import pywt
from utils import downsample

WAVELET = "db4"
TARGET_LEN = 50


def shannon_entropy(coeffs):
    energy = coeffs**2
    p = energy / np.sum(energy)
    return -np.sum(p * np.log(p + 1e-12))


def load_class(folder, label):
    X = []
    y = []

    for fname in sorted(os.listdir(folder)):
        if fname.endswith(".wav"):
            fs, x = wavfile.read(os.path.join(folder, fname))
            x = x.astype(float).flatten()
            x50 = downsample(x, TARGET_LEN)

            cA, cD = pywt.dwt(x50, WAVELET)

            energy_CA = np.sum(cA**2)
            energy_CD = np.sum(cD**2)
            ratio = energy_CD / (energy_CA + 1e-12)

            entropy_CA = shannon_entropy(cA)
            entropy_CD = shannon_entropy(cD)

            features = [
                energy_CA,
                energy_CD,
                ratio,
                entropy_CA,
                entropy_CD
            ]

            X.append(features)
            y.append(label)

    return np.array(X), np.array(y)


def load_dataset():
    X_evet, y_evet = load_class("data/evet", 0)
    X_hayir, y_hayir = load_class("data/hayir", 1)

    X = np.vstack([X_evet, X_hayir])
    y = np.hstack([y_evet, y_hayir])

    print("Feature shape:", X.shape)
    return X, y
