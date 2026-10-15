import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

def pwm_sin(vector):
    x = np.asarray(vector, dtype=float)
    L = len(x)
    Ffund = 60
    Fs = Ffund * L

    # Repetición del patrón (20 períodos)
    X = np.tile(x, 20)

    # Filtrado Butterworth de primer orden
    b, a = signal.butter(1, Ffund * 2 / (Fs / 2), btype='low')
    xf = signal.lfilter(b, a, X)

    # Espectro y búsqueda de picos
    XF = np.abs(np.fft.fft(xf))
    mitad_len = int(np.round(len(XF) / 2))
    localiz, _ = signal.find_peaks(XF[:mitad_len])
    picos = XF[localiz]

    # Cálculo del THD (Distorsión Armónica Total)
    X1 = picos[0] ** 2
    Xr = np.sum(picos[1:] ** 2)
    
    return Xr / X1

# Duda: ¿Forma de la entropía normalizada?
def calc_entropia_norm(P):
    entropia = 0
    for prob in P:
        entropia = entropia - prob * np.log2(prob) # Entropia de Shannon

    entropia_norm = entropia / np.log2(len(P)) # Entropia Normalizada
    return entropia_norm

def LR(entropia, type, k_sig = 10, k_exp = 4):
    if type == "sigmoide":
        return 1 - (1 / (1 + np.exp(-k_sig * (entropia - 0.5))))
    elif type == "lineal":
        return 1 - entropia
    elif type == "exponencial":
        return 1 - ((np.exp(k_exp * entropia) - 1) / (np.exp(k_exp) - 1))

# plt.figure()
# En = np.linspace(1,0,1000)
# plt.plot(En, LR(En, "sigmoide"))
# plt.xlim(1, 0)
# plt.xlabel("Entropía Normalizada")
# plt.ylabel("LR")
# plt.grid()
# plt.show()