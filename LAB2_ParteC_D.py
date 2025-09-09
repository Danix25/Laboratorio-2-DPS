import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# --- 1. Cargar la señal ---
signal = np.loadtxt(r'C:\Users\danil\Downloads\senal.txt')


# --- 2. Graficar la señal ---
fs = 1000  # frecuencia de muestreo en Hz
dt = 1 / fs  # intervalo entre muestras en segundos
t = np.arange(len(signal)) * dt


plt.figure(figsize=(10,4))
plt.plot(t, signal, color='blue')
plt.title("Señal Biológica")
plt.xlabel("Tiempo [S]")
plt.ylabel("Voltaje pico a pico [mV]")
plt.grid(True)
plt.show()

# --- 3. Determinar frecuencia de Nyquist ---
fs_nyquist = 1 / (2 * dt)
fs_sample = 4 * fs_nyquist

print("Frecuencia de Nyquist:", fs_nyquist)
print("Frecuencia de muestreo (4x Nyquist):", fs_sample)

# --- 4. Caracterizar la señal ---
media = np.mean(signal)
mediana = np.median(signal)
std = np.std(signal)
maximo = np.max(signal)
minimo = np.min(signal)

print("\nCaracterización de la señal:")
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", std)
print("Máximo:", maximo)
print("Mínimo:", minimo)

# Clasificación básica
tipo = "Determinística" if np.all(np.diff(signal) != 0) else "Aleatoria"
periodicidad = "Periódica" if np.all(signal[:len(signal)//2] == signal[len(signal)//2:]) else "Cuasi-periódica"
forma = "Analógica"
print("\nClasificación de la señal:")
print("Tipo:", tipo)
print("Periodicidad:", periodicidad)
print("Forma:", forma)

# --- 5. Transformada de Fourier ---
N = len(signal)
yf = fft(signal)
xf = fftfreq(N, 1/fs_sample)

# Graficar transformada y densidad espectral de potencia
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(xf, np.abs(yf), color='red')
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")

plt.subplot(2,1,2)
plt.plot(xf, np.abs(yf)**2, color='green')
plt.title("Densidad espectral de potencia")
plt.xlabel("Frecuencia")
plt.ylabel("Potencia")
plt.tight_layout()
plt.show()

# --- 6. Estadísticos en dominio de la frecuencia ---
amplitud = np.abs(yf)
potencia = amplitud**2
frecuencia_media = np.sum(xf * amplitud) / np.sum(amplitud)
frecuencia_mediana = xf[np.where(np.cumsum(amplitud)/np.sum(amplitud) >= 0.5)[0][0]]
frecuencia_std = np.sqrt(np.sum((xf - frecuencia_media)**2 * amplitud) / np.sum(amplitud))

print("\nEstadísticos en frecuencia:")
print("Frecuencia media:", frecuencia_media)
print("Frecuencia mediana:", frecuencia_mediana)
print("Desviación estándar:", frecuencia_std)

# Histograma de frecuencias
plt.figure(figsize=(10,4))
plt.hist(xf, weights=amplitud, bins=50, color='purple', edgecolor='black')
plt.title("Histograma de frecuencias")
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud acumulada")
plt.grid(True)
plt.show()