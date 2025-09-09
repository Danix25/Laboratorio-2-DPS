# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 12:24:08 2025

@author: danil
"""

import matplotlib.pyplot as plt
import numpy as np

#Señal con datos Daniel
H1=[1,0,1,3,2,5,8,0,9,2]
X1=[5,6,0,0,7,9,0]

#Señal con datos Sara
H2=[1,0,7,6,2,4,0,9,1,9]
X2=[5,6,0,0,7,9,1]

#Señal con datos Paola
H3=[1,0,1,4,2,6,0,8,9,6]
X3=[5,6,6,0,0,6,7,8]

#Para calcular la convolucion de Daniel
Y = np.convolve(X1, H1)

#Para calcular la convolucion de Sara
A = np.convolve(X2, H2)

#Para calcular la convolucion de Paola
B = np.convolve(X3, H3)

#Ejes de tiempo
n_y = np.arange(len(Y))
n_A = np.arange(len(A))
n_B = np.arange(len(B))

print("Resultado convolución para datos Daniel:", Y.tolist() )
print("Resultado convolución para datos Sara:", A.tolist() )
print("Resultado convolución para datos Paola:", B.tolist() )

#Grafica señal resultante de Daniel
plt.figure(figsize=(9,5))
plt. stem(n_y, Y, basefmt= " ")
plt.title("Convolución entre H[n] y X[n] (DANIEL)")
plt.xlabel("Muestras [n]")
plt.ylabel("Y[n]")
plt.grid(True)

#Grafica señal resultante de Sara
plt.figure(figsize=(8,4))
plt. stem(n_A, A, basefmt= " ")
plt.title("Convolución entre H[n] y X[n] (SARA)")
plt.xlabel("Muestras [n]")
plt.ylabel("Y[n]")
plt.grid(True)

#Grafica señal resultante de Paola
plt.figure(figsize=(8,4))
plt. stem(n_B, B, basefmt= " ")
plt.title("Convolución entre H[n] y X[n] (PAOLA)")
plt.xlabel("Muestras [n]")
plt.ylabel("Y[n]")
plt.grid(True)

plt.tight_layout()
plt.show()



