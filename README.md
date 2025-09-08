# Laboratorio-2

prueba 2
# CONVOLUCIÓN, CORRELACIÓN Y TRANSFORMADA DE FOURIER
# TABLA DE CONTENIDOS
1. Objetivos y metodología del experimento.
2. Diagramas de flujo.
3. Adquisición de la señal.
4. Análisis de resultados.
5. Conclusiones.
6. Aplicaciones biomédicas.

# 1. Objetivos y metodología del experimento.
# 2. Diagrama de flujo.
# 3. Adquisición de la señal.
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
 # 4. Análisis de resultados.
 # 5. Conclusiones.
 # 6. Aplicaciones biomédicas.
 
 El cálculo de valores estadísticos en el análisis de señales, es muy útil para su interpretación, ya que nos permite extraer información que facilita comprender su comportamiento y distribución. Esto se puede evidenciar en los siguientes casos vistos en este laboratorio:
 - Convolución:Este tipo de operacion permite realizar los cálculos estadistícos filtrando el ruido presente en las señeles biomedicas,reslatar tambien componentes importantes y facilitar la visualizacion de la señal original para llegar a un analisis confiable.
 - Correlación:En estas aplicacione estos calculos estadísticos nos permiten identificar pateones dentro de una señal,medir el grado de similitud entre diferentes registros tambien localizando los eventos repetittivos,siendo fundamental para el estudio de señales fisiológicas.
 - Transformada de Fourier: Aquí, los calculos estadisticos permiten observar la distribución de la señal en el dominio de la frecuencia,lo que hace posible detectar los componentes periodiocos y analizar la variabilidad de esa señal en diferentes rangos espectrales.
 - Electrooculografía (EOG): En este tipo de señal, los cálculos estadísticos permite analizar los movimientos oculares,cuantificando la activdad de los musculos extraoculares y detectar posibles alteraciones neurologicas o visuales,siendo de gran importancia en estas aplicaciones biomédicas.
