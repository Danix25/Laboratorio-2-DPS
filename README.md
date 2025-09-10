    # Laboratorio-2
# CONVOLUCIÓN, CORRELACIÓN Y TRANSFORMADA DE FOURIER
# TABLA DE CONTENIDOS
1. Objetivos y metodología del experimento.
2. Marco conceptual.
3. Diagramas de flujo.
4. Adquisición de la señal.
5. Análisis de resultados.
6. Conclusiones.
7. Aplicaciones biomédicas.

# 1. Objetivos y metodología del experimento.
La presente práctica tiene como objetivo comrpender el concpeto de convolución y como esta operación permite obtener la respuesta de un sistema discreto ante una entrada determinada. Además, se busca analizar el concepto de correlación y aplicar la transformada de Fourier como una herramienta de análisis en el dominio de la frecuencia.
Lo anteriormente mencionado se hizo empleando técnicas como el cálculo de la convolución de una señal a partir de las identificaciones y códigos de los estudiantes. Además, se hizo el cálculo de la correlación cruzada y la transformada de fourier de una señal de Electrooculografía (EOG), capturada de un generador de señales biológicas para finalmente implementar algoritmos para mostrar los resultados obtenidos.

# 2. Marco conceptual.

**Electrooculografía:** Es una prueba electrofisiológica para valoral el estado funcional de la capas de retina. Aquí se registran las variaciones electricas que se porudcen en el ojo al realizar un movimiento ocular. Esto nos permite confirmar diagnósticos para posibles enfermedades de la retina.

<img width="300" height="500" alt="image" src="https://github.com/user-attachments/assets/b71a31f4-2d16-4daf-8f88-36785958f496" />

**Convolución:** Se refiere a una operación fundamental dentro del procesamiento digital de señales para determinar la salida de un sistema lineal invariante en el tiempo, de acuerdo a una señal de entrada y una respuesta impulso de un sistema.

<img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/957bba5a-f4f4-4630-8ad6-5f9c62aa282a" />

**Correlación cruzada:** Es una herramienta que nos permite medir la similitud entre dos señales en función de un desplazamiento temporal, esto para encontrar un patrón conocido dentro de una señal más larga o identificar tendencias y/o relaciones.

**Transformada de Fourier:** Es una herramienta de gran relevancia dentro del procesamiento digital de señales, en el cual se descompone una señal en sus componentes sinusoidales de diferentes frecuencias, es decri, permite visualizar una señal que está en el dominio del tiempo al dominio de la frecuencia, siendo muy importante para el análisis y estudio de diversas señales.

# 3. Diagrama de flujo.

El siguiente diagrama de flujo muestra el procedimiento utilizado para la adquisición de datos mediante el sistema DAQ, basado en el código desarrollado por la profesora Carolina Corredor.

<img width="310" height="1300" alt="diagramaDAQ" src="https://github.com/user-attachments/assets/03a2c92e-40e8-45d5-a1d4-52178245be13" />

El siguiente diagrama de flujo ilustra el procedimiento implementado para el procesamiento de la señal adquirida, incluyendo el cálculo de estadísticas descriptivas en tiempo y frecuencia, así como el análisis mediante la Transformada de Fourier.

<img width="920" height="1920" alt="Diagrama CODIGO" src="https://github.com/user-attachments/assets/80d9a732-550a-4526-9444-89666129a101" />


# 4. Adquisición de la señal.
La señal de electrooculografía (EOG).

Materiales Utilizados.

- Cables
- Data acquisition (DAQ)
- Generador de señales
- Osciloscopio 
- Cables o jumpers

Se hizo la conexión del DAQ al generador de señales, eL cual también tambien fue conectado a la entrada USB del computador para poder  guardar los datos obtenidos de dicha señal. Esta señal (electrooculografía) la pudimos observar en el osciloscopio, lo que nos permitio verfificar su forma de onda. 

<img src="https://github.com/user-attachments/assets/de167f12-5352-4112-925f-7ed2ff729f89" width="400"/>

Señal obtenidad:

<img src="https://github.com/user-attachments/assets/7e5fd84d-e908-4c53-b3c2-85e02cdc4186" width="400"/>

Código Utilizado:

Se utilizo el sigueinte código para obtener la señal por medio de DAQ y enviarla a la computadora:
```cpp Adquisición de la señal por tiempo definido

fs = 1000          
duracion = 10        
senal = []         
dispositivo = 'Dev1/ai0' 

total_muestras = int(fs * duracion)

with nidaqmx.Task() as task:
    # Configuración del canal
    task.ai_channels.add_ai_voltage_chan(dispositivo)
    # Configuración del reloj de muestreo
    task.timing.cfg_samp_clk_timing(
        fs,
        sample_mode=AcquisitionType.FINITE,   
        samps_per_chan=total_muestras        
    )

    # Lectura de todas las muestras de una vez
    senal = task.read(number_of_samples_per_channel=total_muestras)

t = np.arange(len(senal))/fs # Crea el vector de tiempo 
plt.plot(t,senal)
plt.axis([0,duracion,-10,10])
plt.grid()
plt.title(f"fs={fs}Hz, duración={duracion}s, muestras={len(senal)}")
plt.show()
np.savetxt("senal.txt", senal)
```
 Autor Del Código: Carolina Corredor.
 
 Fecha: 2025-09-09.
 # 5. Análisis de resultados.
 
- **Parte A.**

En primera instancia, se recolectaron las identificaciones y códigos de los estudiantes, para luego ubicarlas en dos señales y calcular la convolución de ellas. Este calculo se hizo de la siguiente manera:

  *1.* Su ubicaban los datos en una tabla (identificación en las filas y código en la columna).

  *2.* Se multiplicaban los datos de la fila por cada columna ( los digitos de la identificación se multiplicaban con el primero digito del código; ej: 1,0,3,5,6 por 5)

  *3.* Se hace la suma de las diagonales de los resultados de las multiplicaciones.

  *4.* El resultado de cada suma es la secuencia resultante de la convolución.

  Esto se hizo para cada estudiante y posterior a ello se graficó cada secuancia, correspondiente a la señal resultante, en las que obtuvieron las siguientes gráficas:

Resultados *Daniel*:

Y[n]: [5, 6, 5, 21, 35, 46, 77, 78, 86, 117, 113, 72, 63, 95, 18, 0]

  <img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/e4425ab7-6803-4558-a8b4-c0675e3719da" />

Resultados *Sara*:

Y[n]: [5, 6, 35, 72, 53, 41, 74, 150, 134, 103, 92, 67, 88, 81, 82, 9]

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/5f555a78-c0e1-4d5e-a616-4b5af4b43dc0" />

Resultados *Paola*:

Y[n]: [5, 6, 11, 26, 40, 72, 55, 90, 124, 180, 172, 94, 96, 110, 163, 114, 48]

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/ffddc16a-f308-4e3b-ad6a-b378f5d96512" />

- **Parte B.**

Para este punto, se definieron las siguientes señales:

<img width="300" height="54" alt="image" src="https://github.com/user-attachments/assets/ec7c6214-2c0e-43c5-a666-2ab5e6afac2e" />

Y posteriormente se graficaron, obteniendo las siguientes gráficas:

<img width="606" height="329" alt="image" src="https://github.com/user-attachments/assets/0af78c0a-66d6-4867-8b74-58cc10d56986" />

<img width="601" height="329" alt="image" src="https://github.com/user-attachments/assets/b76a50b8-674e-4f12-b0d2-1dfc48f4a81f" />

Con base a estas, se hizo el cálculo para la correlación cruzada haciendo uso de la siguiente ecuación:

<img width="318" height="96" alt="image" src="https://github.com/user-attachments/assets/62c963ca-0109-4a40-a511-6c6a4977807e" />

Teniendo en cuenta que **K=N-1**, siendo 8 y según la teoría, la correlación cruzada se usa para los valores positivos y negativos, reemplazando estos en la ecuación inicial. Por eso, la correlación cruzada se da entre -8 a +8. Esto resulta en la siguiente secuencia:

[-2.44929360e-16 -7.07106781e-01 -1.50000000e+00 -1.41421356e+00 -1.66533454e-16  2.12132034e+00  3.50000000e+00  2.82842712e+00
8.81375476e-17 -2.82842712e+00 -3.50000000e+00 -2.12132034e+00  3.33066907e-16  1.41421356e+00  1.50000000e+00  7.07106781e-01  0.00000000e+00]    

Estos valores se reflejan en la siguiente gráfica:

<img width="603" height="329" alt="image" src="https://github.com/user-attachments/assets/b292bf06-3163-4205-866e-0565fbe99202" />

En esta gráfica se observa que el pico más alto está cuando *k*=-2, con un valor de 3.5. Por otro lado, el valor mínimo se ubica cuando *k*=2, también con un valor de 3.5, lo que se puede interpretar que la señal X2[n] está adelantada en 2 muestras respecto a X1[n]. Esto quiere decir que si desplazamos la primera señal dos pasos a la derecha, habrá una mejor similitud con la segunda señal.

Esto refleja la importancia del cálculo de la correlación cruzada en señales, ya que nos permite confirmar de una manera más precisa la similitud estructural entre ellas. Además, aplicar este tipo de técnicas resulta util para conocer la sincronización entre señales, reconocer patrones en ellas y así analizar de una forma más precisa y efectiva la similitud entre señales.

- **Parte C.**

Para este punto, inicialmente se capturó una señal EOG con ayuda de un generador de señales fisiológicas, obteniendo lo siguiente:

<img width="725" height="330" alt="image" src="https://github.com/user-attachments/assets/88b59f8e-a036-45f9-9ea2-e620ec9d9f0e" />

Con una frecuencia de Nyquist de 500 Hz
Posterior a ello se determinó una nueva frecuencia de Nyquist con 4 veces esta frecuencia, siendo de 2000 Hz.
Además, se caracterizó la señal obteniendo la media (0.1591), mediana (0.09215), desviación estandar (0.3799), el máximo (1.4847) y mínimo (-1.3799). Estos resultados nos indican que la señal está bien capturada, ya que no hay una saturación y los eventos son claros. Además, la desviación estándar frente a los picos son eventos esporádicos dominantes, siendo normal para una señal EOG. Sin embargo, la media al ser ligeramente positiva, indica que se deberia corregir el offset DC para prevenir errores en un análisis más detallado. 

Además de esto, se clasificó la señal, siendo esta como una señal aleatoria (al ser una señal biológica, puede tener fluctuaciones o ser impredecible), digital (Ya que se muestra en ejes discretos) y cuasí-periodica (Muestra oscilaciones repetitivas, pero no idénticas siendo caracteristico en señales biológicas).

Luego de la caracterización, para hacer un análisis más detallado, se aplicó la transformada de Fourier para conocer la densidad espectral y el comportamiento de la señal en el dominio de la frecuencia, en lo que obtuvimos las siguientes gráficas:

<img width="672" height="327" alt="image" src="https://github.com/user-attachments/assets/3f170f78-20db-4295-b1a4-e33879c775c7" />

Con base a estos resultados, se puede percibir una simetría en la señal alrededor de 0 Hz, con un ancho de banda observable, ya que entre más se aleja de los 0 Hz, disminuye la energía util en la señal y esto es normal para las señales EOG, ya que la energía util de estas está por debajo de los 30 o 50 Hz. Lo mismo sucede con la densidad espectral, ya que más alla de 100 Hz aproximadamente, la densidad espectral es muy baja. Además de esto, abordando una interpretación más especifica con las señales EOG convencionales, la señal capturada refleja un EOG típico, la cual se caracteriza por ser de predominante baja frecuencia.

Finalmente, se hizo el cálculo de los estadísticos en frecuencia, donde se obtuvo la frecuencia media (-0.4555), frecuencia mediana (962.2) y desviación estandar (46.1158), lo que nos dice que la señal está centrada en bajas frecuencias. Sin embargo, con la frecuencia mediana, al tener un valor tan alto, se puede asumir como un error de cálculo, hay una presencia de ruido o artefacto que pueda "empujar" la distribución de la mediana, ya que para estas señales la energía está en bajas frecuencias. Esto mismo sucede con la desviación estnadar, ya que significa que la señal no está concentrada en una sola banda, sino que tiene dispersión hacia frecuencias medias o altas.

 # 6. Conclusiones.

 A través del cálculo manual y gráfico de las convoluciones entre las señales definidas con identificaciones y códigos, se entendió cómo esta operación matemática permite modelar la respuesta de un sistema discreto ante diferentes entradas. Los resultados obtenidos muestran cómo la convolución combina la información de ambas señales.

La adquisición de la señal de electrooculografía con el DAQ permitió ver su forma de onda y obtener parámetros estadísticos relevantes (media: 0.1591, desviación estándar: 0.3799, máximo: 1.4847, mínimo: -1.3799).

La señal de Electrooculografía (EOG) adquirida con una frecuencia de muestreo de 1000 Hz y duración de 10 segundos fue caracterizada estadísticamente en el dominio del tiempo con una media de 0.1591, mediana de 0.09215 y desviación estándar de 0.3799, indicadores que muestran que la señal está bien tomada.

Este laboratorio permitió integrar la teoría con la práctica en señales biomédicas. La convolución mostró cómo se obtiene la salida de un sistema, la correlación ayudó a medir la similitud temporal entre señales y la transformada de Fourier permitió descomponer y estudiar la distribución espectral.

 # 7. Aplicaciones biomédicas.
 
 El cálculo de valores estadísticos en el análisis de señales, es muy útil para su interpretación, ya que nos permite extraer información que facilita comprender su comportamiento y distribución. Esto se puede evidenciar en los siguientes casos vistos en este laboratorio:
 - Convolución:Este tipo de operacion permite realizar los cálculos estadistícos filtrando el ruido presente en las señeles biomedicas,reslatar tambien componentes importantes y facilitar la visualizacion de la señal original para llegar a un analisis confiable.
 - Correlación:En estas aplicacione estos calculos estadísticos nos permiten identificar pateones dentro de una señal,medir el grado de similitud entre diferentes registros tambien localizando los eventos repetittivos,siendo fundamental para el estudio de señales fisiológicas.
 - Transformada de Fourier: Aquí, los calculos estadisticos permiten observar la distribución de la señal en el dominio de la frecuencia,lo que hace posible detectar los componentes periodiocos y analizar la variabilidad de esa señal en diferentes rangos espectrales.
 - Electrooculografía (EOG): En este tipo de señal, los cálculos estadísticos permite analizar los movimientos oculares,cuantificando la activdad de los musculos extraoculares y detectar posibles alteraciones neurologicas o visuales,siendo de gran importancia en estas aplicaciones biomédicas.

**CÁLCULOS A MANO**

<img width="200" height="600" alt="image" src="https://github.com/user-attachments/assets/ebc48aa5-87a8-4411-bee0-b3c9fdeb12c7" />

<img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/da9a97db-29cf-40f3-9c69-198dc72ac3eb" />

<img width="401" height="324" alt="image" src="https://github.com/user-attachments/assets/28266f06-1acd-48a5-a3b3-16964e9637f5" />

<img width="347" height="212" alt="image" src="https://github.com/user-attachments/assets/cde005d1-111e-418c-85dd-e7d808eef29c" />

<img width="364" height="213" alt="image" src="https://github.com/user-attachments/assets/3c59713a-6acd-43ff-8a38-ad8caa4f3db6" />

<img width="300" height="229" alt="image" src="https://github.com/user-attachments/assets/15fde09c-f719-4710-853d-77b2b107af9e" />

<img width="369" height="182" alt="image" src="https://github.com/user-attachments/assets/b9e85509-2200-4b20-a5f8-c6588dadfe08" />

<img width="427" height="246" alt="image" src="https://github.com/user-attachments/assets/2c86fd7f-3b42-45f8-9e15-1f0d14357d44" />

<img width="447" height="189" alt="image" src="https://github.com/user-attachments/assets/514f3a5f-75ef-424b-a42c-c124180e2f1b" />

<img width="200" height="150" alt="image" src="https://github.com/user-attachments/assets/c9fd73d1-0005-47bd-915a-18f535729637" />



