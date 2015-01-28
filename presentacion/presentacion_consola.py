#!/usr/local/bin/python3.4

from abc import ABCMeta, abstractclassmethod
import os
import collections
import adquisidor
import procesador
import modelo
import persistidor
import utilidades
import configurador

from datetime import datetime
from modelo.senial import Senial
from configurador.configurador import Configurador


class Pantalla(metaclass=ABCMeta):

    def __init__(self, titulo):
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
                if items_opciones[int(op) - 1] == "Volver":
                    break
                else:
                    self._opciones[items_opciones[int(op) - 1]].mostrar()


class PantallaInfo(Pantalla):

    def mostrar(self):
        self.mostrar_titulo()


class PantallaInfoVersiones(PantallaInfo):

    def mostrar(self):
        super().mostrar()
        print("adquisidor: " + adquisidor.__version__)
        print("procesador: " + procesador.__version__)
        print("persistidor: " + persistidor.__version__)
        print("configurador: " + configurador.__version__)
        print("modelo: " + modelo.__version__)
        print("utiles: " + utilidades.__version__)
        print()
        self.tecla()


class PantallaInfoComponentes(PantallaInfo):
    def mostrar(self):
        super().mostrar()
        print("Tipo adquisidor: ", Configurador.adquisidor.__class__)
        print("Tipo procesador: ", Configurador.procesador.__class__)
        print()
        self.tecla()


class PantallaAccion(Pantalla):

    def mostrar(self):
        super().mostrar_titulo()


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


class PantallaAccionProcesamiento(PantallaAccion):

    def mostrar(self):
        super().mostrar()
        '''Paso 2 - Se procesa la señal adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        print()
        id_senial = input("Ingresar el identificador de la señial:")
        rep_adq = Configurador.rep_adquisicion
        rep_pro = Configurador.rep_procesamiento
        p = Configurador.procesador
        senial_a_procesar = rep_adq.obtener(Senial(), id_senial)
        p.procesar(senial_a_procesar)
        sp = p.obtener_senial_procesada()
        self.tecla()
        print('Se persiste la señal procesada')
        sp.comentario = input('Descripcion de la señal procesada:')
        sp.id = int(input('Identificacion (nro entero)'))
        rep_pro.guardar(sp)
        print('Señal Guardada')
        self.tecla()


class PantallaAccionVisualizacion(PantallaAccion):

    def mostrar(self):
        super().mostrar()
        print("Incio - Paso 3 - Mostrar Senial")
        id_senial_adq = input("Ingresar el identificador de la señial adquirida:")
        id_senial_pro = input("Ingresar el identificador de la señial procesada:")
        rep_adq = Configurador.rep_adquisicion
        rep_pro = Configurador.rep_procesamiento
        adquirida = rep_adq.obtener(Senial(), id_senial_adq)
        procesada = rep_pro.obtener(Senial(), id_senial_pro)
        print("{0:20s}{1:s}".format("Adquirida", "Procesada"))
        for i in range(0, adquirida.cantidad):
            print("{0:f}{1:20f}".format(adquirida.obtener_valor(i), procesada.obtener_valor(i)))
        self.tecla()


class AplicacionSOLID(object):

    @classmethod
    def iniciar(cls):
        p_adquisicion = PantallaAccionAdquisicion("Adquisicion de la Señal")
        p_procesamiento = PantallaAccionProcesamiento("Procesamiento de la Señal")
        p_visualizacion = PantallaAccionVisualizacion("Visualizacion de la Señal")

        op_menu_aplicacion = collections.OrderedDict()
        op_menu_aplicacion["Adquidir Señal"] = p_adquisicion
        op_menu_aplicacion["Procesar Señal"] = p_procesamiento
        op_menu_aplicacion["Visualizar Señal"] = p_visualizacion
        op_menu_aplicacion["Volver"] = None

        p_configuracion = PantallaInfoComponentes("Configuracion de elementos")
        p_versiones = PantallaInfoVersiones("Versiones de los componentes")
        p_acerca_de = PantallaInfo("Acerca")
        p_menu_aplicacion = PantallaMenu("Aplicacion", op_menu_aplicacion)
        p_salir = PantallaAccionFin("Salir")

        op_menu_principal = collections.OrderedDict()
        op_menu_principal["Configuracion"] = p_configuracion
        op_menu_principal["Versiones"] = p_versiones
        op_menu_principal["Aplicacion"] = p_menu_aplicacion
        op_menu_principal["Acerca de"] = p_acerca_de
        op_menu_principal["Salir"] = p_salir

        p_menu_principal = PantallaMenu("Principal", op_menu_principal)

        print(os.getcwd())
        p_menu_principal.mostrar()