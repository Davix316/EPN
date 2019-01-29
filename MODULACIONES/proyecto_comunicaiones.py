import pygame
import sys, pygame
from pygame.locals import *
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from math import *
from mod_AM import *
from tkinter import *
import sys

#########




reloj = pygame.time.Clock()
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


class Menu:
    "Representa un menú con opciones para un juego"

    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font(None, 40)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False


    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                print("Selecciona la opción '%s'." % (titulo))
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""
        fuente = pygame.font.Font(None, 40)
        titulo = fuente.render("DIFERENTES TIPOS DE MODULACIÓN Y DEMODULACIÓN ", True, AZUL)
        # Coloca la imagen del texto sobre la pantalla en 250 x 250
        screen.blit(titulo, [90, 25])

        total = self.total
        indice = 0
        altura_de_opcion = 70
        x = 510# posicion de la letras en x
        y = 88 # posicion de las letras en y

        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (ROJO)
            else:
                color = (BLANCO)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)


##############INICIO DE DESARROLLO DE FUNCIONES###################

def crear_nueva_pantalla():
    pygame.init()
    screen = pygame.display.set_mode((950, 510))
    pygame.display.set_caption("..............ONDAS..........!!")
    screen.fill(BLANCO)
    fondo_menu2 = pygame.image.load("Imagenes/FONDO.jpg").convert()
    screen.blit(fondo_menu2, (0, 0))
    fuente = pygame.font.Font(None, 30)
    reg = fuente.render("R=regresar", True, NEGRO)

    screen.blit(reg, [760, 480])
    iconReturn = pygame.image.load("Imagenes/RE.png").convert()
    screen.blit(iconReturn, (886, 447))

def cerrar_ventana():


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == pygame.K_x:
                        salir_del_programa()
                if evento.key == pygame.K_r:
                        regresar()


        pygame.display.update()

def regresar():
    print("vuelve a la pag principal")
    if __name__ == '__main__':

        salir = False
        opciones = [
            ("AM", mod_dem_AM),
            ("FM", mod_dem_FM),
            ("PCM", mod_dem_PCM),
            ("ASK", mod_dem_ASK),
            ("FSK", mod_dem_FSK),
            ("PSK", mod_dem_PSK),
            ("QAM", mod_dem_QAM),
            ("Salir", salir_del_programa)
        ]

        ##########3

        ######

        pygame.font.init()
        screen = pygame.display.set_mode((1100, 650))
        pygame.display.set_caption("PROYECTO COMUNICACIONES")
        fondo = pygame.image.load("Imagenes/4.jpg").convert()
        fondo2 = pygame.image.load("Imagenes/menu.png")
        title = pygame.image.load("Imagenes/title.png")

        pygame.display.set_icon(pygame.image.load("Imagenes/icono.png").convert_alpha())  # icono del juego
        relojmenu = pygame.time.Clock()

        menu = Menu(opciones)
        ###var globales

        ### fin var global

        while not salir:

            for e in pygame.event.get():
                if e.type == QUIT:
                    salir = True

            screen.blit(fondo, (30, 10))
            screen.blit(fondo2, (400, 70))
            screen.blit(title, (50, 5))
            # screen.blit(mapa_menu, (130, 200))
            # screen.blit(imagen_opciones,(125,250))
            menu.actualizar()
            menu.imprimir(screen)

            pygame.display.flip()
            pygame.time.delay(10)


def mod_dem_AM():
    print ("FUNCION de modulacion y demodulacion AM")
    select=opciones
    crear_nueva_pantalla()
    subopc1 = fuente.render("1: Modulación AM ", True, BLANCO)
    subopc2 = fuente.render("2: Demodulación AM ", True, BLANCO)
    screen.blit(subopc1, [630, 120])
    screen.blit(subopc2, [630, 170])

    LEFT = 1

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == pygame.K_1:
                    modulacion_AM()
                if evento.key == pygame.K_2:
                    #demodulacion_AM()
                    print("demodulacion")
                if evento.key == pygame.K_x:
                        salir_del_programa()
                if evento.key == pygame.K_r:
                        regresar()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT:

                print("You pressed the right mouse button at (%d, %d)" % evento.pos)
                print(" izquirdo")
                #modulacion_AM()

        pygame.display.update()

   # cerrar_ventana()

def mod_dem_FM():
    print(" mod y demod fm")

    ######texto en la 2 pantalla

    crear_nueva_pantalla()

    subopc1 = fuente.render("1: Modulación FM ", True, BLANCO)
    subopc2 = fuente.render("2: Demodulación FM ", True, BLANCO)
    screen.blit(subopc1, [630, 120])
    screen.blit(subopc2, [630, 170])
    cerrar_ventana()
def mod_dem_PCM():
    print(" mod y demod PCM")
    crear_nueva_pantalla()
    ######texto en la 2 pantalla

    subopc1 = fuente.render("1: Modulación PCM ", True, BLANCO)
    subopc2 = fuente.render("2: Demodulación PCM ", True, BLANCO)
    screen.blit(subopc1, [630, 120])
    screen.blit(subopc2, [630, 170])
    cerrar_ventana()


def mod_dem_ASK ():
    print(" mod y demod ASK")
    crear_nueva_pantalla()
    ######texto en la 2 pantalla

    subopc1 = fuente.render("1: Modulación ASK ", True, BLANCO)
    subopc2 = fuente.render("2: Demodulación ASK ", True, BLANCO)
    screen.blit(subopc1, [630, 120])
    screen.blit(subopc2, [630, 170])
    cerrar_ventana()

def  mod_dem_FSK ():
    print (" mod y demod FSK")
    crear_nueva_pantalla()
    subopc1 = fuente.render("1: Modulación FSK ", True, BLANCO)
    subopc2 = fuente.render("2: Demodulación FSK ", True, BLANCO)
    screen.blit(subopc1, [630, 120])
    screen.blit(subopc2, [630, 170])
    cerrar_ventana()
    #

def mod_dem_PSK ():
    print (" mod y demod PSK")
    crear_nueva_pantalla()

    subopc1 = fuente.render("1: Modulación PSK ", True, BLANCO)
    subopc2 = fuente.render("2: Demodulación PSK ", True, BLANCO)
    screen.blit(subopc1, [630, 120])
    screen.blit(subopc2, [630, 170])
    cerrar_ventana()

def mod_dem_QAM ():
    print (" mod y demod QAM")

    crear_nueva_pantalla()

    subopc1 = fuente.render("1: Modulación QAM ", True, BLANCO)
    subopc2 = fuente.render("2: Demodulación QAM ", True, BLANCO)
    screen.blit(subopc1, [630, 120])
    screen.blit(subopc2, [630, 170])
    cerrar_ventana()

def salir_del_programa():
    import sys
    print(" Gracias por utilizar este programa.")
    sys.exit(0)

###############



############


if __name__ == '__main__':


    salir = False
    opciones = [
        ("AM", mod_dem_AM),
        ("FM", mod_dem_FM),
        ("PCM", mod_dem_PCM),
        ("ASK", mod_dem_ASK),
        ("FSK", mod_dem_FSK),
        ("PSK", mod_dem_PSK),
        ("QAM", mod_dem_QAM),
        ("Salir", salir_del_programa)
    ]

    ##########3

    ######

    pygame.font.init()
    screen = pygame.display.set_mode((1100, 650))
    pygame.display.set_caption("PROYECTO COMUNICACIONES")
    fondo = pygame.image.load("Imagenes/4.jpg").convert()
    fondo2 = pygame.image.load("Imagenes/menu.png")
    title = pygame.image.load("Imagenes/title.png")
    fuente = pygame.font.Font(None, 37)
    pygame.display.set_icon(pygame.image.load("Imagenes/icono.png").convert_alpha())# icono del juego
    relojmenu = pygame.time.Clock()

    menu = Menu(opciones)
    ###var globales


    ### fin var global

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (30, 10))
        screen.blit(fondo2, (400,70))
        screen.blit(title, (50, 5))
        #screen.blit(mapa_menu, (130, 200))
        #screen.blit(imagen_opciones,(125,250))
        menu.actualizar()
        menu.imprimir(screen)


        pygame.display.flip()
        pygame.time.delay(10)
        ###


