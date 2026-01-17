# Librerie varie che ci serovono
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Titolo e descrizione dell'app
st.title("Analisi di Fourier di un segnale")
st.write("Segnale sinusoidale e spettro in frequenza")

T = 1     # Durata

# Menù a tendina per scegliere il tipo di segnale
option = st.selectbox("Tipo di segnale", ["Sinusoide",
                                          "Cosinusoide", "Somma di sinusoidi"])

# Slider per la freq di campionamento
Fs = st.slider("Frequenza di campionamento (Hz)", 50, 1000, 200)
t = np.arange(0, T, 1/Fs)


# Creazione del segnale in base alla scelta
if option == "Somma di sinusoidi":

    # Slider delle due sinusoidi
    A1 = st.slider("Ampiezza", 0.1, 5.0, 1.0)          # Ampiezza
    f1 = st.slider("Frequenza (Hz)", 1, 50, 5)         # Frequenza (in Hz)
    A2 = st.slider("Ampiezza 2", 0.1, 5.0, 1.0)        # Ampiezza
    f2 = st.slider("Frequenza (Hz) 2", 1, 50, 5)       # Frequenza (in Hz)

    # Somma di una sinusoide e una cosinusoide
    x = (A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.cos(2 * np.pi * f2 * t))

elif option == "Cosinusoide":
    A = st.slider("Ampiezza", 0.1, 5.0, 1.0)          # Ampiezza
    f = st.slider("Frequenza (Hz)", 1, 50, 5)         # Frequenza (in Hz)

    # Segnale cosinusoidale
    x = A * np.cos(2 * np.pi * f * t)

elif option == "Sinusoide":
    A = st.slider("Ampiezza", 0.1, 5.0, 1.0)          # Ampiezza
    f = st.slider("Frequenza (Hz)", 1, 50, 5)         # Frequenza (in Hz)

    # Segnali sinusoidale
    x = A * np.sin(2 * np.pi * f * t)

# Calcolo della FFT (DFT tramite algoritmo FFT)
X = np.fft.fft(x)

# Creazione dell'asse delle frequenze
N = len(x)                              # Numero di campioni
freq = np.fft.fftfreq(N, 1/Fs)          # Frequenze associate alla FFT
freq_pos = freq[:N//2]                  # Prendo solo la metà positiva

# Spettro monolatero
# Segnali reali -> simmetria coniugata della FFT
X_pos = X[:N//2]
# Modulo e normalizzazione
# Moltiplico per due per conservare la stessa energia su frequenze positive fino a Fs/2 (Nyquist)
M_pos = 2 * np.abs(X_pos) / N


# Grafico del segnale nel dominio del tempo
fig, ax = plt.subplots()
ax.set_title("Segnale nel tempo")
ax.set_xlabel("Tempo [s]")
ax.set_ylabel("Ampiezza")
ax.plot(t, x)

# Grafico dello spettro in frequenza
fig2, bx = plt.subplots()
bx.set_title("Spettro di ampiezza")
bx.set_xlabel("Frequenza [Hz]")
bx.set_ylabel("|X(f)|")
bx.plot(freq_pos, M_pos)

# Li pongo in due colonne diverse
st.pyplot(fig)
st.pyplot(fig2)
