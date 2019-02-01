import numpy as np # L
import matplotlib.pyplot as plt

#----MODULACION POR CAMBIO DE FRECUENCIA FSK------
#--- SE BASA EN CAMBIOS BINARIO DE O Y 1
# ingresa dos señales sinusoidales y va comparando con un proceso for:
# para poder modular la señal
#utiliza dos  señales del mismo tipo
def modulacion_FSK():

    v = [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1] ##genera vector binario de 11 digitos
    dim = 100 # numero de muestras a tomar
    Vx = [] # donde se almacena los elementos para lu7ego graficar
    Di = []
    f1 = 5  # frecuencia 1
    f2 = 20 # frecuencia 2

    for i in range(1, 11):  # barrido de los espacios del vetor v creado  trabaja de 1 a 11 debido a que tiene 11 digitos
        f = np.ones(dim)  # variable
        x = f * v[i]  # vector q multiplica  la variable f con cada  elemento de las  las posiciones  del vector v
        Vx = np.concatenate((Vx, x))# llenaos el vector vacio con la union de los dos vectores vx y x

    #------- INCIO DE GRAFICA 1-----
    plt.subplot(4, 1, 1) # 4 grafica  1 figura primera posicion (4=filas,1=col,1=grafica)
    plt.title("Señal de Impulso binario", family='Times New Roman', fontsize=12)## binario o logico  y 1 logico
    plt.xlabel("tiempo [s]", family='Times New Roman')
    plt.ylabel("amplitud [v]", family='Times New Roman')
    plt.plot(Vx,'b',linewidth=1) # grafica la señal Vx
    tam = len(Vx)
    t = np.linspace(0, 5, tam)

    #------FIN----

    #------- INCIO DE GRAFICA 2-----

    plt.subplot(4, 1, 2)# 4 grafica  1 figura segunda posicion 4=filas,1=col,2=grafica)
    plt.title("primera Onda Portadora", family='Times New Roman', fontsize=12)
    plt.xlabel("tiempo [s]", family='Times New Roman')
    plt.ylabel("amplitud [v]", family='Times New Roman')
    w1 = 2 * np.pi * f1 * t
    y1 = np.cos(w1) # funcion coseno para la primera señal
    plt.plot(t, y1,'g',linewidth=0.8)
    #------FIN----

    #------- INCIO DE GRAFICA 3-----

    plt.subplot(4, 1, 3) # 4 grafica  1 figura tercera posicion 4=filas,1=col,grafica 3)
    plt.title("Segunda onda portadora", family='Times New Roman', fontsize=12)
    plt.xlabel("tiempo [s]", family='Times New Roman')
    plt.ylabel("amplitud [v]", family='Times New Roman')
    w2 = 2 * np.pi * f2 * t
    y2 = np.cos(w2) # funcion coseno con  valor de la frecuencia 2   de la segunda señal
    plt.plot(t, y2,'m',linewidth=0.8) #imprime la funcion escrita la posicion en x = tiempo , y
    #------FIN----

    #------iNICIO DE GRAFICA 4----

    plt.subplot(4, 1, 4) # 4 grafica  1 figura cuarta posicion 4=filas,1=col,4=grafica)
    plt.title("Señal modulada FSK", family='Times New Roman', fontsize=12)
    plt.xlabel("tiempo [s] ", family='Times New Roman')
    plt.ylabel("amplitud [v]", family='Times New Roman')
    for i in range(0, tam): #incio de for  con rando desde 0 y salto de 2
        if Vx[i] == 0: #validacion de los eleemtos del vector Vx ==0 si cumple pasa a la siguiente linea
            cero = np.array([y2[i]]) #  va a realizar el array de ceros
            Di = np.concatenate((Di, cero))
        else: # caso contrario
            uno = np.array([y1[i]]) # el vector desplazamiento esta en 1
            Di = np.concatenate((Di, uno)) # une las
    plt.plot(t, Di,'c',linewidth=0.6)
    #-----FIN-----
    plt.show() #  metodo que muestra en pantalla las graficas realizadas

if __name__ == '__main__':
     modulacion_FSK()