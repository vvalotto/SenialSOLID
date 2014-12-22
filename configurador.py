"""
Configura la clase que se usara
"""
from procesador.procesador import *
from adquisidor.adquisidor import *
from visualizador.visualizador import *


def definir_procesador():
    return ProcesadorConUmbral(20)

def definir_adquisidor():
    return AdquisidorSimple(5)

def definir_visualizador():
    return Visualizador()

class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    adquisidor = definir_adquisidor() #Se configura el tipo de adquisidor
    procesador = definir_procesador() #Se configura el tipo de procesador
    visualizador = definir_visualizador() #Se configura el visualizador

    def __init__(self):
        pass

