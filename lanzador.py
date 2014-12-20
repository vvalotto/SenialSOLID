"""
Ejemplo de solucion para el SRP, donde las responsabilidades se dividen
entre diferentes clases.
"""
import os
from senial_solid.adquisidor import *
from senial_solid.procesador import *
from senial_solid.visualizador import *


class ProgramaSRP():
    """
    Programa Lanzador
    """
    def __init__(self):
        pass

    @staticmethod
    def tecla():
        """
        Funcion que solicita un tecla para continuar
        """
        while True:
            if input('C para continuar> ') == "C":
                break
        return

    # noinspection PyShadowingNames
    def ejecutar(self):
        """
        Se instancian las clases que participan del procesamiento
        """
        a = Adquisidor(5)
        p = Procesador()
        v = Visualizador()

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        a.leer_senial()
        sa = a.obtener_senial_adquirida()
        self.tecla()

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        p.procesar_senial(sa)
        sp = p.obtener_senial_procesada()
        self.tecla()

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        v.mostrar_datos(sp)
        print("Fin Programa - SRP")


if __name__ == "__main__":
    ProgramaSRP().ejecutar()