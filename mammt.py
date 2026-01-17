import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Titolo e descrizione dell'app
st.title("Analisi di Fourier di un segnale")
st.write("Segnale sinusoidale e spettro in frequenza")

# Slider per la frequenza di campionamento
Fs = st.slider("Frequenza di campionamento (Hz)", 50, 1000, 200)
T = 1  # Durata
t = np.arange(0, T, 1/Fs)

# Creazione di colonne per menu + slider
col_menu, col_param = st.columns([1, 2])

with col_menu:
    option = st.selectbox("Tipo di segnale", [
                          "Sinusoide", "Cosinusoide", "Somma di sinusoidi"])

with col_param:
    # Slider dipendenti dalla scelta
    if option == "Sinusoide":
        A = st.slider("Ampiezza", 0.1, 5.0, 1.0)
        f = st.slider("Frequenza (Hz)", 1, 50, 5)
        x = A * np.sin(2 * np.pi * f * t)

    elif option == "Cosinusoide":
        A = st.slider("Ampiezza", 0.1, 5.0, 1.0)
        f = st.slider("Frequenza (Hz)", 1, 50, 5)
        x = A * np.cos(2 * np.pi * f * t)

    elif option == "Somma di sinusoidi":
        A1 = st.slider("Ampiezza 1", 0.1, 5.0, 1.0)
        f1 = st.slider("Frequenza 1 (Hz)", 1, 50, 5)
        A2 = st.slider("Ampiezza 2", 0.1, 5.0, 1.0)
        f2 = st.slider("Frequenza 2 (Hz)", 1, 50, 5)
        x = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.cos(2 * np.pi * f2 * t)

# Calcolo della FFT
X = np.fft.fft(x)
N = len(x)
freq = np.fft.fftfreq(N, 1/Fs)
freq_pos = freq[:N//2]

# Spettro monolatero
X_pos = X[:N//2]
M_pos = 2 * np.abs(X_pos) / N

# Grafici in colonne separate
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.plot(t, x)
    ax.set_title("Segnale nel tempo")
    ax.set_xlabel("Tempo [s]")
    ax.set_ylabel("Ampiezza")
    ax.grid(True)
    st.pyplot(fig)

with col2:
    fig2, bx = plt.subplots()
    bx.plot(freq_pos, M_pos)
    bx.set_title("Spettro di ampiezza")
    bx.set_xlabel("Frequenza [Hz]")
    bx.set_ylabel("|X(f)|")
    bx.grid(True)
    st.pyplot(fig2)
