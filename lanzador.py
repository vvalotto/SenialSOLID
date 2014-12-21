#!/usr/local/bin/python3.4
"""
Ejemplo de solucion para el SRP, donde las responsabilidades se dividen
entre diferentes clases.
"""
import os
import adquisidor
import procesador
import visualizador
import modelo

from adquisidor.adquisidor import *
from procesador.procesador import *
from visualizador.visualizador import *


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
    def seleccionar_procesador():
        """
        Pide al usuario la seleccion del tipo de procesador
        """
        os.system("clear")
        print("Seleccionar tipo de procesamiento:")
        print("1 > Valor Doble")
        print("2 > Umbral")
        while True:
            op = input('Opcion: ')
            if op in ['1', '2']:
                break
        return op

    @staticmethod
    def informar_versiones():
        """
        Informa las versiones actuales de cada modulo
        """
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
        tipo_pro = Lanzador.seleccionar_procesador()

        a = Adquisidor(5)
        p = Procesador()
        v = Visualizador()

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        a.leer_senial()
        sa = a.obtener_senial_adquirida()
        Lanzador.tecla()

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        if tipo_pro == '1':
            p.procesar_senial(sa)
        elif tipo_pro == '2':
            p.procesar_senial_con_umbral(sa)
        else:
            print('Sin procesador selecionado')
            print("Fin Programa - NoOCP")
            exit()
        sp = p.obtener_senial_procesada()
        Lanzador.tecla()

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        v.mostrar_datos(sp)
        print("Fin Programa - NoOCP")


if __name__ == "__main__":
    Lanzador().ejecutar()