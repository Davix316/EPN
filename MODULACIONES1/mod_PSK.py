import numpy as np
import matplotlib.pyplot as plt
from math import*

def modulacion_PSK():
    v = [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1] #vector unitario
    dim=100 #numero de muestras a tomar en el pulso unitario
    Vx=[] #vector vacio donde se almacenan los elementos

    # Señal unitaria de pulsos binarios
    for i in range (1,11):
        f=np.ones(dim) #vector creado lleno de 1
        x=f*v[i]
        Vx=np.concatenate((Vx,x))
    plt.subplot(4,1,1)
    plt.plot(Vx)

    # Señal de informacion 1
    dim2=len(Vx)
    t=np.linspace(0,5,dim2)
    #Funcion cos
    f1=2
    plt.subplot(4,1,2)
    w1=2*np.pi*f1*t
    y1=np.cos(w1)
    plt.plot(t,y1)

    # Señal de informacion 2
    # Funcion sin
    f2=2
    plt.subplot(4,1,3)
    w2=2*np.pi*f2*t
    y2=np.sin(w2)
    plt.plot(t,y2)

    # Señal modulada
    plt.subplot(4,1,4)
    res=((y2*Vx)-(y1*Vx)+(y1))
    plt.plot(t,res)
    plt.show()

if __name__ == '__main__':
     modulacion_PSK()