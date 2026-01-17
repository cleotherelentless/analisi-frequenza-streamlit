import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("Analisi di Fourier di un segnale")
st.write("Segnale sinusoidale, cosinusoidale, somma di sinusoidi o da CSV e spettro in frequenza")

# --- Modalità segnale ---
mode = st.radio("Seleziona modalità segnale:", [
                "Genera segnale", "Carica CSV"])

T = 1  # durata per segnale generato

if mode == "Genera segnale":
    option = st.selectbox("Tipo di segnale", [
                          "Sinusoide", "Cosinusoide", "Somma di sinusoidi"])
    Fs = st.slider("Frequenza di campionamento (Hz)", 50, 1000, 200)
    t = np.arange(0, T, 1/Fs)

    if option == "Somma di sinusoidi":
        A1 = st.slider("Ampiezza 1", 0.1, 5.0, 1.0)
        f1 = st.slider("Frequenza 1 (Hz)", 1, 50, 5)
        A2 = st.slider("Ampiezza 2", 0.1, 5.0, 1.0)
        f2 = st.slider("Frequenza 2 (Hz)", 1, 50, 5)
        x = A1 * np.sin(2*np.pi*f1*t) + A2 * np.cos(2*np.pi*f2*t)

    elif option == "Cosinusoide":
        A = st.slider("Ampiezza", 0.1, 5.0, 1.0)
        f = st.slider("Frequenza (Hz)", 1, 50, 5)
        x = A * np.cos(2*np.pi*f*t)

    elif option == "Sinusoide":
        A = st.slider("Ampiezza", 0.1, 5.0, 1.0)
        f = st.slider("Frequenza (Hz)", 1, 50, 5)
        x = A * np.sin(2*np.pi*f*t)

elif mode == "Carica CSV":
    uploaded_file = st.file_uploader("Carica file CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Anteprima dei dati:", df.head())

        if 'tempo' in df.columns:
            t = df['tempo'].to_numpy()
        else:
            Fs = st.slider("Frequenza di campionamento (Hz)", 50, 1000, 200)
            T = len(df)/Fs
            t = np.arange(0, T, 1/Fs)

        amp_col = st.selectbox("Seleziona colonna del segnale:", df.columns)
        x = df[amp_col].to_numpy()
    else:
        st.stop()  # se non caricato, fermo l'app
else:
    st.stop()

# --- Calcolo FFT ---
N = len(x)
X = np.fft.fft(x)
freq = np.fft.fftfreq(N, t[1]-t[0])
X_pos = X[:N//2]
freq_pos = freq[:N//2]
M_pos = 2 * np.abs(X_pos) / N

# --- Grafico tempo e frequenza con Plotly ---
fig_time = px.line(x=t, y=x, labels={
                   'x': 'Tempo [s]', 'y': 'Ampiezza'}, title='Segnale nel tempo')
fig_time.update_layout(plot_bgcolor='#0E1117', paper_bgcolor='#0E1117')

fig_freq = px.line(x=freq_pos, y=M_pos, labels={
                   'x': 'Frequenza [Hz]', 'y': 'Ampiezza'}, title='Spettro monolatero')
fig_freq.update_layout(plot_bgcolor='#0E1117', paper_bgcolor='#0E1117')

# --- Layout colonne ---

st.plotly_chart(fig_time, use_container_width=True)
st.plotly_chart(fig_freq, use_container_width=True)
