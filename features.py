"""
Bu kodun amacı, ham ses dalgalarını doğrudan kullanmak yerine, onları anlamlı feature'lara dönüştürmektir.
"""
import os
import numpy as np
from scipy.io import wavfile
import pywt # DWT islemleri
from utils import downsample

WAVELET = "db4" # Kullanılacak dalgacık tipi (Daubechies 4)
TARGET_LEN = 50 # Tüm seslerin indirgenecegi hedef uzunluk

def shannon_entropy(coeffs):
    energy = coeffs**2
    p = energy / np.sum(energy) # Normalizasyon
    return -np.sum(p * np.log(p + 1e-12))

def load_class(folder, label):
    X = []
    y = []
# Dosya okuma
    for fname in sorted(os.listdir(folder)):
        if fname.endswith(".wav"):
            fs, x = wavfile.read(os.path.join(folder, fname))
            x = x.astype(float).flatten()
            x50 = downsample(x, TARGET_LEN)
            
# Approximation ve Detail coeffs olarak sinyali iki parcaya ayirir
            cA, cD = pywt.dwt(x50, WAVELET)
# Her ses için 5 adet feature üretilir
            energy_CA = np.sum(cA**2)
            energy_CD = np.sum(cD**2)
            ratio = energy_CD / (energy_CA + 1e-12)
"""
Eğer bu oran (ratio) yüksekse, enerji "Detay (yüksek frekans)" katsayılarına daha çok dağılmış demektir. Bu da o sesin daha sürtünmeli veya gürültülü (örneğin "f", "s", "h" gibi harfler içeren) bir ses olduğunu makineye anlatır.
"""
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
    X_evet, y_evet = load_class("data/evet", 0) # Evet'lere 0 etiketi
    X_hayir, y_hayir = load_class("data/hayir", 1) # Hayır'lara 1 etiketi

    X = np.vstack([X_evet, X_hayir]) # Özellikleri alt alta 
    y = np.hstack([y_evet, y_hayir]) # Etiketleri yan yana birleştirir

    print("Feature shape:", X.shape)
    return X, y

