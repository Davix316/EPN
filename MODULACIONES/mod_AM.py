import matplotlib.pyplot as plt
import numpy as np
from numpy import*
from math import*


def modulacion_AM():

    Fc=300
    t=np.arange(0,0.1,10**(-5.7))
    x=np.sin(40*pi*t)
    w=np.sin(2*Fc*pi*t)
    p=w*x
    y=(t,p)
    plt.subplot(311)
    plt.plot(t,x,linewidth=0.4)
    plt.xlabel("indice de tiempo")
    plt.ylabel("amplitud")
    plt.subplot(312)
    plt.plot(t,w,linewidth=0.4)
    plt.ylabel("amplitud")
    plt.subplot(313)
    plt.xlabel("indice de tiempo")
    plt.ylabel("amplitud")
    plt.title("modulacion am de la señal", fontsize=12)
    plt.plot(t,p,linewidth=0.4)
    plt.show()

if __name__ == '__main__':
     modulacion_AM()

