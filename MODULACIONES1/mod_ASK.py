import numpy as np
import matplotlib.pyplot as plt
from math import*

def modulacion_ASK():
    v=[1,0,1,1,0,1] #vector unitario
    dim=100 #numero de muestras a tomar en el pulso unitario
    Vx=[] #vector vacio donde se almacenan los elementos

    #Señal unitaria de pulsos binarios
    for i in range (1,6):
        f=np.ones(dim) #vector creado lleno de 1
        x=f*v[i] #vector nuevo donde se multiplica cada posicion continuamente en el ciclo for
        Vx=np.concatenate((Vx,x)) #se llena vector vacio al unir 2 vectores
    plt.subplot(3,1,1)
    plt.plot(Vx)

    #Señal de informacion
    dim2=len(Vx)  # segunda dimension que recorre el espacio de la onda senosoidal
    t=np.linspace(0,5,dim2)#linea de tiempo en saltos de dimension 2
    f1=5#frecuencia para la señal
    plt.subplot(3,1,2)# grafica senusoidal que lleva la informacion
    w1=2*np.pi*f1*t #argumento de la señal
    y1=np.cos(w1) #señal coseno del argumento
    plt.plot(t,y1)

    #Señal modulada
    plt.subplot(3, 1, 3)
    mult=Vx*y1 #vector unitario por señal coseno
    plt.plot(t,mult)
    plt.show()

if __name__ == '__main__':
     modulacion_ASK()