"""
Configura la clase que se usara
"""
from procesador.procesador import *


def definir_procesador():
    return ProcesadorConUmbral(20)


class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    procesador = definir_procesador() #Se configura el tipo de procesador

    def __init__(self):
        pass

