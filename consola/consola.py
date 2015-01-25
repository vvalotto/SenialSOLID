#!/usr/local/bin/python3.4

from abc import ABCMeta, abstractclassmethod
import os
import adquisidor
import procesador
import visualizador
import modelo
import persistidor
import utilidades
from configurador import *

class Pantalla(metaclass=ABCMeta):

    def __init__(self, titulo,):
        self._titulo = titulo
        pass

    @abstractclassmethod
    def mostrar(self):
        pass

    def mostrar_titulo(self):
        os.system("clear")
        print(self._titulo)
        print('-' * len(self._titulo))
        print()


    def tecla(self):
        """
        Funcion que solicita un tecla para continuar
        """
        while True:
            if input('C para continuar> ') == "C":
                break
        return

class PantallaMenu(Pantalla):

    def __init__(self, titulo, opciones):
        super().__init__(titulo)
        self._opciones = opciones
        pass

    def mostrar_opciones(self):
        items_op = []
        for op in self._opciones:
            items_op.append(op)

        for i in range(0, len(items_op)):
            print("{0} > {1}".format(i + 1, items_op[i]))

    def mostrar(self):
        """
        Genera la pantalla de opciones
        """
        while True:
            self.mostrar_titulo()
            self.mostrar_opciones()
            items_opciones = []
            for opcion in self._opciones:
                items_opciones.append(opcion)
            lista_id_opciones = []
            for i in range(0, len(items_opciones)):
                lista_id_opciones.append(str(i + 1))
            op = input('Elija una opcion > ')
            if op in lista_id_opciones:
                self._opciones[items_opciones[int(op) - 1]].mostrar()


class PantallaInfo(Pantalla):

    def mostrar(self):
        self.mostrar_titulo()


class PantallaInfoVersiones(PantallaInfo):

    def mostrar(self):
        super().mostrar()
        print("adquisidor: " + adquisidor.__version__)
        print("procesador: " + procesador.__version__)
        print("visualizador: " + visualizador.__version__)
        print("persistidor: " + persistidor.__version__)
        print("modelo: " + modelo.__version__)
        print("utiles: " + utilidades.__version__)
        print()
        self.tecla()

class PantallaInfoComponentes(PantallaInfo):
    def mostrar(self):
        super().mostrar()
        print("Tipo adquisidor: ", Configurador.adquisidor.__class__)
        print("Tipp procesador: ", Configurador.procesador.__class__)
        print()
        self.tecla()

class PantallaAccion(Pantalla):

    def mostrar(self):
        self.mostrar_titulo()


class PantallaAccionFin(PantallaAccion):

    def mostrar(self):
        super().mostrar()
        print("Fin del programa")
        exit()

class PantallaAccionAdquisicion(PantallaAccion):

    def mostrar(self):
        super().mostrar()
        '''Paso 1 - Se obtiene la señal'''
        a = Configurador.adquisidor
        rep_adq = Configurador.rep_adquisicion
        a.leer_senial()
        sa = a.obtener_senial_adquirida()
        sa.fecha_adquisicion = datetime.datetime.now().date()
        sa.comentario = input('Descripcion de la señal:')
        sa.id = int(input('Identificacion (nro entero):'))
        print('Fecha de lectura: {0}'.format(sa.fecha_adquisicion))
        print('Cantidad de valores obtenidos {0}'.format(sa.cantidad))
        self.tecla()
        print('Se persiste la señal adquirida')
        rep_adq.guardar(sa)
        print('Señal Guardada')
        self.tecla()


if __name__ == "__main__":

    p_adquisicion = PantallaAccionAdquisicion("Adquisicion de la Señal")
    p_procesamiento = PantallaAccion("Procesamiento de la Señal")
    p_visualizacion = PantallaAccion("Visualizacion de la Señal")

    op_menu_aplicacion = {}
    op_menu_aplicacion["Adquidir Señal"] = p_adquisicion
    op_menu_aplicacion["Procesar Señal"] = p_procesamiento
    op_menu_aplicacion["Visualizar Señal"] = p_visualizacion

    p_configuracion = PantallaInfoComponentes("Configuracion de elementos")
    p_versiones = PantallaInfoVersiones("Versiones de los componentes")
    p_acerca_de = PantallaInfo("Acerca")
    p_menu_aplicacion = PantallaMenu("Aplicacion", op_menu_aplicacion)
    p_salir = PantallaAccion("Salir")

    op_menu_principal = {}
    op_menu_principal["Configuracion"] = p_configuracion
    op_menu_principal["Versiones"] = p_versiones
    op_menu_principal["Acerca de"] = p_acerca_de
    op_menu_principal["Aplicacion"] = p_menu_aplicacion
    op_menu_principal["Salir"] = p_salir

    p_menu_principal = PantallaMenu("Principal", op_menu_principal)
    p_menu_principal.mostrar()
