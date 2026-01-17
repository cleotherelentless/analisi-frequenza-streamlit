import numpy as np
import matplotlib.pyplot as plt

# Parametri del segnale sinusoidale
A = 1          # Ampiezza
f = 5         # Frequenza (in Hz)
Fs = 200       # Frequenza di campionamento (Hz)
T = 1          # Durata

# Creazione dell'asse dei tempi
t = np.arange(0, T, 1/Fs)

# Creazione del segnale sinusoidale
x = A * np.sin(2 * np.pi * f * t)

# Visualizzazione del segnale
plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.title('Skibidibobbi')
plt.xlabel('Tempo (s)')
plt.ylabel('Ampiezza')
plt.grid(True)
plt.show()

# Verifica conettuale
# 1) Se aumento f, le oscillazioni sono più veloci
# 2) Se aumento Fs, la sinusoide diventa più continua
# 3) NYQUIST: DSe Fs < 2f si verifica aliasing, cioè il segnale campionato appare come un segnale a frequenza diversa da quella reale
