"""
Configura la clase que se usara
"""
from xml.dom import minidom
from procesador.procesador import *
from adquisidor.adquisidor import *
from visualizador.visualizador import *
from persistidor.repositorio import *
from persistidor.contexto import *
from modelo.senial import *


def definir_senial_adquirir():
    return SenialPila(100)


def definir_senial_procesar():
    return SenialPila(100)


def definir_procesador():
    return Procesador(definir_senial_procesar())


def definir_adquisidor():
    return AdquisidorSenoidal(definir_senial_adquirir())


def definir_visualizador():
    return Visualizador()


def definir_contexto(recurso):
    return ContextoPickle(recurso)


def definir_repositorio(contexto):
    return RepositorioSenial(contexto)


def obtener_dir_datos():
    try:
        conf = minidom.parse("./datos/configuracion.xml")
        dir_datos = conf.getElementsByTagName("dir_datos")[0]
        return dir_datos.firstChild.data
    except Exception as ex:
        raise ex


def obtener_dir_adquisicion():
    try:
        conf = minidom.parse("./datos/configuracion.xml")
        dir_datos = conf.getElementsByTagName("dir_entrada_datos")[0]
        return dir_datos.firstChild.data
    except Exception as ex:
        raise ex


class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    ctx_datos_adquisicion = definir_contexto(obtener_dir_datos() + '/adq')
    ctx_datos_procesamiento = definir_contexto(obtener_dir_datos() + '/pro')

    rep_adquisicion = definir_repositorio(ctx_datos_adquisicion)
    rep_procesamiento = definir_repositorio(ctx_datos_procesamiento)

    adquisidor = definir_adquisidor()  # Se configura el tipo de adquisidor
    procesador = definir_procesador()  # Se configura el tipo de procesador
    visualizador = definir_visualizador()  # Se configura el visualizador

    def __init__(self):
        pass
