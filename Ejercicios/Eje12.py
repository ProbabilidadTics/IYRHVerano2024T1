import numpy as np
import matplotlib.pyplot as plt

def histograma_calorías(datos, num_clases=6):
  
    plt.figure(figsize=(10,6))
    plt.hist(datos, bins=num_clases, edgecolor='black')
    plt.xlabel('Calorías')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Calorías en Sándwiches')
    plt.show()
