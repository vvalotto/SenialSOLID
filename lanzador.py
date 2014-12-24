#!/usr/local/bin/python3.4
__author__ = 'Victor Valotto'
__version__ = '6.0.0'

"""
Ejemplo de solucion para el SRP, donde las responsabilidades se dividen
entre diferentes clases.
"""
import os
import adquisidor
import procesador
import visualizador
import modelo

from configurador import *




class Lanzador():
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

    @staticmethod
    def informar_versiones():
        os.system("clear")
        print("Versiones de los componenetes")
        print("adquisidor: " + adquisidor.__version__)
        print("procesador: " + procesador.__version__)
        print("visualizador: " + visualizador.__version__)
        print("modelo: " + modelo.__version__)

    @staticmethod
    def ejecutar():
        """
        Se instancian las clases que participan del procesamiento
        """
        Lanzador.informar_versiones()
        Lanzador.tecla()

        a = Configurador.adquisidor
        p = Configurador.procesador
        v = Configurador.visualizador

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        a.leer_senial()
        sa = a.obtener_senial_adquirida()
        print(sa.tamanio)
        Lanzador.tecla()

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        p.procesar(sa)
        sp = p.obtener_senial_procesada()
        Lanzador.tecla()

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        v.mostrar_datos(sp)
        print('----->')
        for i in range(0, sp.tamanio):
            print(sp.sacar_valor())

        print("Fin Programa - LSP")


if __name__ == "__main__":
    Lanzador().ejecutar()