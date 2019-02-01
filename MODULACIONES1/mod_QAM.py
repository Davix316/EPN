import matplotlib.pyplot as plt# libreria encargada de graficar en la pantalla de python
import numpy as np
from math  import*

def modulacion_QAM():


    t = np.arange(0, 0.1, 10 ** (-5.7))
    #---funcion coseno---
    fc = 100
    Ac = 1
    v_cos = Ac * np.cos(2 * pi * fc * t) # variable almacena la funcion del seno
    #---- funcion del seno
    As = 1;
    v_sen = As * np.sin(2 * pi * fc * t)

    ##Modulacion de la onda en QAM-----##
    mod = -1 * v_cos + 0.6 * v_sen  ## variable almacena la suma de las dos señales declaradas anteriormente seno y coseno

    #-- primera grafica
    plt.subplot(3, 1, 1) # 3 filas 1 colum y la grafica en la primera posicion
    plt.plot(t, v_cos,'b')
    plt.ylabel("amplitud", family='Times New Roman')  # titulo  de la grafica onda moduladora en el eje y
    plt.xlabel("indice de tiempo")  #
    plt.title('señal del coseno',family='Times New Roman', fontsize=12)
    ## segunda grafica----
    plt.subplot(3, 1, 2)# 3 filas 1 col  y la grafica en la segunda posicion
    plt.plot(t, v_sen,'r')
    plt.ylabel("amplitud", family='Times New Roman')  # titulo  de la grafica onda moduladora en el eje y
    plt.xlabel("indice de tiempo")  #
    plt.title('Señal seno',family='Times New Roman', fontsize=12)

    # trecera grafica----
    plt.subplot(3, 1, 3) # 3 graficas 1 figura posicion 3
    plt.plot(t, mod,'y')
    plt.ylabel("amplitud", family='Times New Roman')  # titulo  de la grafica onda moduladora en el eje y
    plt.xlabel("indice de tiempo")  #
    plt.title('Señal modulada en QAM',family='Times New Roman', fontsize=12)
    plt.show()

if __name__ == '__main__':
     modulacion_QAM()