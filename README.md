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

<img width="407" height="750" alt="image" src="https://github.com/user-attachments/assets/b71a31f4-2d16-4daf-8f88-36785958f496" />

**Convolución:** Se refiere a una operación fundamental dentro del procesamiento digital de señales para determinar la salida de un sistema lineal invariante en el tiempo, de acuerdo a una señal de entrada y una respuesta impulso de un sistema.

<img width="686" height="386" alt="image" src="https://github.com/user-attachments/assets/957bba5a-f4f4-4630-8ad6-5f9c62aa282a" />

**Correlación cruzada:** Es una herramienta que nos permite medir la similitud entre dos señales en función de un desplazamiento temporal, esto para encontrar un patrón conocido dentro de una señal más larga o identificar tendencias y/o relaciones.

**Transformada de Fourier:** Es una herramienta de gran relevancia dentro del procesamiento digital de señales, en el cual se descompone una señal en sus componentes sinusoidales de diferentes frecuencias, es decri, permite visualizar una señal que está en el dominio del tiempo al dominio de la frecuencia, siendo muy importante para el análisis y estudio de diversas señales.

# 3. Diagrama de flujo.
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
 
- **Parte A:** En primera instancia, se recolectaron las identificaciones y códigos de los estudiantes, para luego ubicarlas en dos señales y calcular la convolución de ellas. Este calculo se hizo de la siguiente manera:
  *1.* Su ubicaban los datos en una tabla (identificación en las filas y código en la columna).
  *2.* Se multiplicaban los datos de la fila por cada columna ( los digitos de la identificación se multiplicaban con el primero digito del código; ej: 1,0,3,5,6 por 5)
  *3.* Se hace la suma de las diagonales de los resultados de las multiplicaciones.
  *4.* El resultado de cada suma es la secuencia resultante de la convolución.

  Esto se hizo para cada estudiante y posterior a ello se graficó cada secuancia, correspondiente a la señal resultante, en las que obtuvieron las siguientes gráficas:

Resultados Daniel:

Y[n]: [5, 6, 5, 21, 35, 46, 77, 78, 86, 117, 113, 72, 63, 95, 18, 0]

  <img width="542" height="329" alt="image" src="https://github.com/user-attachments/assets/e4425ab7-6803-4558-a8b4-c0675e3719da" />

Resultados Sara:

Y[n]: [5, 6, 35, 72, 53, 41, 74, 150, 134, 103, 92, 67, 88, 81, 82, 9]

<img width="585" height="326" alt="image" src="https://github.com/user-attachments/assets/5f555a78-c0e1-4d5e-a616-4b5af4b43dc0" />

Resultados Paola:

Y[n]: [5, 6, 11, 26, 40, 72, 55, 90, 124, 180, 172, 94, 96, 110, 163, 114, 48]

<img width="670" height="324" alt="image" src="https://github.com/user-attachments/assets/ffddc16a-f308-4e3b-ad6a-b378f5d96512" />

- **Parte B:**
 # 6. Conclusiones.
 # 7. Aplicaciones biomédicas.
 
 El cálculo de valores estadísticos en el análisis de señ-ales, es muy útil para su interpretación, ya que nos permite extraer información que facilita comprender su comportamiento y distribución. Esto se puede evidenciar en los siguientes casos vistos en este laboratorio:
 - Convolución:Este tipo de operacion permite realizar los cálculos estadistícos filtrando el ruido presente en las señeles biomedicas,reslatar tambien componentes importantes y facilitar la visualizacion de la señal original para llegar a un analisis confiable.
 - Correlación:En estas aplicacione estos calculos estadísticos nos permiten identificar pateones dentro de una señal,medir el grado de similitud entre diferentes registros tambien localizando los eventos repetittivos,siendo fundamental para el estudio de señales fisiológicas.
 - Transformada de Fourier: Aquí, los calculos estadisticos permiten observar la distribución de la señal en el dominio de la frecuencia,lo que hace posible detectar los componentes periodiocos y analizar la variabilidad de esa señal en diferentes rangos espectrales.
 - Electrooculografía (EOG): En este tipo de señal, los cálculos estadísticos permite analizar los movimientos oculares,cuantificando la activdad de los musculos extraoculares y detectar posibles alteraciones neurologicas o visuales,siendo de gran importancia en estas aplicaciones biomédicas.
