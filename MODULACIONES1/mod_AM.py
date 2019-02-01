from math  import*
import matplotlib.pyplot as plt# importa la libreri matplotlib para poder graficar
import numpy as np  # importar libreria numpy  con el metodo np para grafica de ondas sinusoidal


def modulacion_AM(): #  inicio de la funcion de modulacion AM

    Fc=300 ## variable de frecuencia : rango de frecuencia = 300
    t=np.arange(0,0.1,10**(-5.7)) ## variable que almacena el tiempo y el rango en q van a dibujarse las graficas
    x=np.sin(40*pi*t) # funcion de la onda moduladora
    w=np.sin(2*Fc*pi*t) #funcion de la onda portadora
    p=w*x # la variable p almacena la onda modula
    y=(t,p)
    #-------. PRIMERA GRAFICA ONDA MODULADORA--------
    plt.subplot(311) # 3 graficas , 1 figura , primera posicion
    plt.title("Onda moduladora", family='Times New Roman', fontsize=12) # titulo de la grafica
    plt.ylabel("amplitud",family='Times New Roman') # titulo  de la grafica onda moduladora en el eje y
    plt.xlabel("indice de tiempo") # titulo  de la grafica onda moduladora en el eje X
    plt.plot(t,x,'b',linewidth=0.4)  # grafica en pantalla  la funcion de la onda almacenda en x y  en tiempo t y controla la liena a un grosor de .4
  ##-------- FIN DE LA PRIMERA GRAFICA--------

    # -------. SEGUNDA GRAFICA ONDA PORTADORA--------
    plt.subplot(312)   ## 3 graficas , 1 figura , Segunda posicion
    plt.plot(t,w,'r',linewidth=0.4)  # grafica en pantalla  la funcion de la onda almacenda en w y  en tiempo t y controla la liena a un grosor de .4

    plt.title("Onda portadora", family='Times New Roman', fontsize=12) # titulo de la segunda grafica
    plt.ylabel("amplitud",family='Times New Roman') # titulo  de la grafica onda portadora en el eje y
    plt.xlabel("indice de tiempo") # titulo  de la grafica onda portadora en el eje x

    #--------FIN DE CODIGO DE LA SEGUNDA GRAFICA------

     #-------TERCERA GRAFICA ONDA MODULADA EN AMPLITUD ----
    plt.subplot(313)## 3 graficas , 1 figura , tercera posicion
    plt.ylabel("amplitud",family='Times New Roman')# titulo  de la grafica onda modulada en el eje y con tipo de letra Times
    plt.xlabel("Tiempo [s]",family='Times New Roman')# titulo  de la grafica onda modulada en el eje x
    plt.title("modulacion AM de la señal",family='Times New Roman',fontsize=12) ## titulo de la tercera Onda (Onda modula en amplitud
    plt.plot(t,p,'g',linewidth=0.4) # grafica  la funcion almacenada en p la misma q se forma entre la union de la onda moduladora y la onda portadora
                                    # en el intervalo de tiempo t definido al inicio , color de linea de la grafica verde se define con la letra 'g'
    plt.show() #metodo para mostrar en pantalla las 3 graficas
    # --------FIN DE CODIGO DE LA TERCERA GRAFICA------

if __name__ == '__main__':
     modulacion_AM()

