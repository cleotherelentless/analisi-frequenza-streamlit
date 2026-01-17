# Librerie varie che ci serovono
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px

# Titolo e descrizione dell'app
st.title("Analisi di Fourier di un segnale")
st.write("Segnale sinusoidale e spettro in frequenza")

# Opzione scelta segnale
mode = st.radio("Seleziona modalità segnale:", [
                "Genera segnale", "Carica CSV"])

T = 1     # Durata del segnale in secondi

if mode == "Genera segnale":
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
        x = A * np.cos(2 * np.pi * f * t)

    elif option == "Sinusoide":
        A = st.slider("Ampiezza", 0.1, 5.0, 1.0)          # Ampiezza
        f = st.slider("Frequenza (Hz)", 1, 50, 5)         # Frequenza (in Hz)
        x = A * np.sin(2 * np.pi * f * t)

elif mode == "Carica CSV":
    # Caricamento CSV
    uploaded_file = st.file_uploader("Carica file CSV", type="csv")
    Fs = st.slider("Frequenza di campionamento (Hz)", 50, 1000, 200)

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Anteprima dei dati:", df.head())

        # Se esiste la colonna 'tempo', la uso e calcolo Fs
        if 'tempo' in df.columns:
            t = df['tempo'].to_numpy()
            Fs = 1 / (t[1] - t[0])
        else:
            # Altrimenti creo un asse dei tempi uniforme
            T = len(df)/Fs
            t = np.arange(0, T, 1/Fs)

        # Menu per scegliere quale colonna usare come segnale
        amp_col = st.selectbox("Seleziona colonna del segnale:", df.columns)
        x = df[amp_col].to_numpy()
    else:
        st.stop()           # Ferma l'esecuzione se nessun CSV viene caricato


# Calcolo della FFT (DFT tramite algoritmo FFT)
X = np.fft.fft(x)

# Creazione dell'asse delle frequenze
N = len(x)                              # Numero di campioni
freq = np.fft.fftfreq(N, 1/Fs)          # Frequenze associate alla FFT
# Prendo solo la metà positiva (monolatero)
freq_pos = freq[:N//2]

# Spettro monolatero
# Segnali reali -> simmetria coniugata della FFT
X_pos = X[:N//2]
# Modulo e normalizzazione
# Moltiplico per due per conservare la stessa energia su frequenze positive fino a Fs/2 (Nyquist)
M_pos = 2 * np.abs(X_pos) / N


# Grafici del segnale nel dominio del tempo e della frequenza
fig_1 = px.line(x=t, y=x, labels={
                'x': 'Tempo [s]', 'y': 'Ampiezza'}, title="Segnale")
fig_2 = px.line(x=freq_pos, y=M_pos, labels={
                'x': 'Frequenza [Hz]', 'y': 'X(f)|'}, title="Spettro di ampiezza")

# Plotta il grafico
st.plotly_chart(fig_1, use_container_width=True)
st.plotly_chart(fig_2, use_container_width=True)
