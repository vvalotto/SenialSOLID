"""
Configura la clase que se usara
"""
from procesador.procesador import *
from adquisidor.adquisidor import *
from visualizador.visualizador import *
from modelo.senial import *
import os


def definir_senial_adquirir():
    return Senial()


def definir_senial_procesar():
    return Senial()


def definir_procesador():
    return ProcesadorConUmbral(20, definir_senial_procesar())


def definir_adquisidor():
    return AdquisidorArchivo('/Users/voval/tmp/adquisidor/datos.txt', definir_senial_adquirir())


def definir_visualizador():
    return Visualizador()


class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    adquisidor = definir_adquisidor()  # Se configura el tipo de adquisidor
    procesador = definir_procesador()  # Se configura el tipo de procesador
    visualizador = definir_visualizador()  # Se configura el visualizador

    def __init__(self):
        pass
