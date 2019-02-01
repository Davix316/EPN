import numpy as np
import matplotlib.pyplot as plt

def modulacion_FM():
    modulator_frequency = 6 #Frecuencia moduladora
    carrier_frequency = 60 #Frecuencia de carga
    modulation_index = 2 #Indice de modulacion o rango

    time = np.arange(44100.0) / 44100.0 #rango del tiempo
    modulator = np.sin(2 * np.pi * modulator_frequency * time) * modulation_index #formula para la señal del mensaje
    carrier = np.sin(2 * np.pi * carrier_frequency * time) #formula de la señal portadora
    product = np.zeros_like(modulator) #Producto para la señal modulada

    for i, t in enumerate(time): #Numero de repeticiones en el tiempo
        product[i] = np.sin(2 * np.pi * (carrier_frequency * t + modulator[i]))

    plt.subplot(3, 1, 1)
    plt.title('Frecuencia Modulada')
    plt.plot(modulator)
    plt.ylabel('Amplitud')
    plt.xlabel('Señal de mensaje')

    plt.subplot(3, 1, 2)
    plt.plot(carrier)
    plt.ylabel('Amplitud')
    plt.xlabel('Señal portadora')

    plt.subplot(3, 1, 3)
    plt.plot(product)
    plt.ylabel('Amplitud')
    plt.xlabel('Señal modulada')
    plt.show()

if __name__ == '__main__':
     modulacion_FM()
