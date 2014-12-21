"""
Para OCP
Se refactoriza la clase de manera de extender otros tipos de
funciones de procesmiento de datos sin que impacte en los anteriores programas
o que cambiando solo las clases de alto nivel que pueda "armar" la solucion
"""
from abc import ABCMeta, abstractmethod
from Modelo.senial import *


class BaseProcesador(metaclass=ABCMeta):
    """
    Clase Abstracta Procesador
    """
    def __init__(self):
        """
        Se inicializa con la senial que se va a procesar
        """
        self._senial_procesada = Senial()
        return

    @abstractmethod
    def procesar(self, senial):
        """
        Método abstracto que se implementara para cada tipo de procesamiento
        """
        pass

    def obtener_senial_procesada(self):
        """
        Devuelve la señal procesada
        """
        return self._senial_procesada


class Procesador(BaseProcesador):
    """
    Clase Procesador simple
    """
    def procesar(self, senial):
        """
        Implementa el procesamiento de duplicar el valor se cada valor de senial
        :param senial:
        :return:
        """
        print("Procesando...")
        for i in range(0, senial.tamanio):
            self._senial_procesada.poner_valor(senial.obtener_valor(i) * 2)
        return


class ProcesadorConUmbral(BaseProcesador):
    """
    Clase Procesador con Umbral
    """
    def __init__(self, umbral):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el umbral
        :param umbral:
        :return:
        """
        BaseProcesador.__init__(self)
        self._umbral = umbral

    def procesar(self, senial):
        """
        Implementa el procesamiento de la senial con umbral
        :param senial:
        :return:
        """
        print("Procesando con umbral")
        for i in range(0, senial.tamanio):
            if senial.obtener_valor(i) < self._umbral:
                self._senial_procesada.poner_valor(senial.obtener_valor(i))
            else:
                self._senial_procesada.poner_valor(0)
        return