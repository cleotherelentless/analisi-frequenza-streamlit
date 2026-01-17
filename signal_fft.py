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
# plt.figure(figsize=(10, 4))
# plt.plot(t, x)
# plt.title('Skibidibobbi')
# plt.xlabel('Tempo (s)')
# plt.ylabel('Ampiezza')
# plt.grid(True)
# plt.show()

# Verifica conettuale
# 1) Se aumento f, le oscillazioni sono più veloci
# 2) Se aumento Fs, la sinusoide diventa più continua
# 3) NYQUIST: DSe Fs < 2f si verifica aliasing, cioè il segnale campionato appare come un segnale a frequenza diversa da quella reale

# Creazione della DTFT
X = np.fft.fft(x)

# Creazione dell'asse delle frequenze
N = len(x)
freq = np.fft.fftfreq(N, 1/Fs)
freq_pos = freq[:N//2]

# Spettro monolatero
# Bisogna prendere solo la prima metà della FFT!! Infatti se x è reale, la FFT ha simmetria coniugata!!
X_pos = X[:N//2]
# Moltiplichiamo per due per conservare la stessa energia complessiva
M_pos = 2 * np.abs(X_pos) / N


plt.figure(figsize=(10, 4))
plt.plot(freq_pos, M_pos)
plt.title('Spettro monolatero del segnale sinusoidale')
plt.xlabel('Frequenza (Hz)')
plt.ylabel('Ampiezza')
plt.grid(True)
plt.show()

# Risposte
# 1) Se raddoppio f, il picco avviene a una frequenza più alta
# 2) Se aumento T -> frequenza più definita -> picco più stretto
# 3) Se Fs diminuisce -> non campiono le oscillazioni veloci -> ho una frequenza più bassa di quella reale
