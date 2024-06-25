import numpy as np
import matplotlib.pyplot as plt


def ojiva_calorías(datos):
  
    sorted_datos = sorted(datos)
    cumulative_freq = [sum(sorted_datos[:i+1]) for i in range(len(sorted_datos))]
    plt.figure(figsize=(10,6))
    plt.plot(sorted_datos, cumulative_freq)
    plt.xlabel('Calorías')
    plt.ylabel('Frecuencia acumulada')
    plt.title('Ojiva de Calorías en Sándwiches')
    plt.show()