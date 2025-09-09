# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 11:59:44 2025

@author: danil
"""

import matplotlib.pyplot as plt
import numpy as np

Ts= 1.25e-3
F= 100
n= np.arange(9)

X1= np.cos(2*np.pi*F*n*Ts)
X2= np.sin(2*np.pi*F*n*Ts)

#Para la correlación cruzada
r = np.correlate(X1, X2, mode='full')

lags= np.arange(-(len(X1)-1), len(X1))

print("lags:", lags)
print("Correlación cruzada:", r)

#Para graficar señal 1
plt.figure(figsize=(8,4))
plt. stem(n, X1, basefmt= " ")
plt.title("Señal X1[n]")
plt.xlabel("Muestras [n]")
plt.ylabel("X1[n]")
plt.grid(True)

#Para graficar señal 2
plt.figure(figsize=(8,4))
plt. stem(n, X2, basefmt=" ")
plt.title("Señal X2[n]")
plt.xlabel("Muestras [n]")
plt.ylabel("X2[n]")
plt.grid(True)

#Para graficar la correlación cruzada
plt.figure(figsize=(9,5))
plt.stem(lags, r, basefmt= " ")
plt.title("Correlación cruzada entre X1[n] y X2[n]")
plt. xlabel("Desplazamiento k")
plt.ylabel("correlación")
plt.grid(True)
    
plt.show()

