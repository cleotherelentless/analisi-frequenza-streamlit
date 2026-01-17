# Analisi di Fourier dei Segnali con Streamlit

**Web app online:** https://hdmjmk2xgzlptwtfkxfr7j.streamlit.app/

Web app interattiva per generare segnali sinusoidali/cosinusoidali oppure caricarli da file CSV e visualizzare lo spettro in frequenza tramite la Trasformata di Fourier (FFT).

L'applicazione è realizzata in Python utilizzando _Streamlit_, _NumPy_, _Pandas_ e _Plotly_.

## Funzionalità

- Generazione di segnali:
  - sinusoide
  - cosinusoide
  - somma di sinusoidi
- Caricamento di segnali da file CSV
- Visualizzazione:
  - segnale nel dominio del tempo
  - spettro di ampiezza (FFT monolatera)
- Interfaccia interattiva tramite slider e menu a tendina

## Contenuto del repository

- `app.py` → script principale dell'app Streamlit
- `dati.csv` → esempio di file CSV contenente un segnale
- `requirements.txt` → librerie Python necessarie
- `README.md` → descrizione del progetto

## Esecuzione locale

1. Clona il repository:
   ```bash
   git clone https://github.com/USERNAME/NOME-REPO.git
   ```
2. Installa le dipendenze:
   pip install -r requirements.txt
3. Avvia l'app:
   streamlit run app.py
