import numpy as np

def downsample(x, target_len=50):
    idx = np.linspace(0, len(x)-1, target_len).astype(int)
    return x[idx]

def normalize(X):
    Xn = np.zeros_like(X)
    for i in range(X.shape[0]):
        Xn[i] = (X[i] - X[i].min()) / (X[i].max() - X[i].min() + 1e-8)
    return Xn
