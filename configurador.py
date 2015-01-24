"""
Configura la clase que se usara
"""
from xml.dom import minidom
from modelo.factory_senial import *
from procesador.factory_procesador import *
from adquisidor.factory_adquisidor import *
from visualizador.visualizador import *
from persistidor.repositorio import *
from persistidor.contexto import *


def obtener_dir_datos():
    try:
        conf = minidom.parse("./datos/configuracion.xml")
        dir_datos = conf.getElementsByTagName("dir_datos")[0]
        return dir_datos.firstChild.data
    except IOError as ex:
        raise ex


def definir_senial_adquirir():
    try:
        # Parsea el xml de configuracion
        conf_procesador = minidom.parse("./datos/configuracion.xml")
        # Busca el nodo de la senial para adquirir
        item_senial_adquirida = conf_procesador.getElementsByTagName("senial_adq")[0]
        # Obtiene el nombre del tipo de senial
        senial = item_senial_adquirida.firstChild.data.strip()
        # Busca los nodos de los parametros
        item_tamanio = item_senial_adquirida.getElementsByTagName("tamanio")[0]
        # Llena la lista con los parametros asociados a la senial
        tamanio = item_tamanio.firstChild.data.strip()
        # Crea el procesador
        return FactorySenial.obtener_senial(senial, tamanio)
    except Exception as ex:
        raise ex


def definir_senial_procesar():
    try:
        # Parsea el xml de configuracion
        conf_procesador = minidom.parse("./datos/configuracion.xml")
        # Busca el nodo del senial a procesar
        item_senial_adquirida = conf_procesador.getElementsByTagName("senial_pro")[0]
        # Obtiene el nombre del tipo de senial
        senial = item_senial_adquirida.firstChild.data.strip()
        # Busca los nodos de los parametros
        item_tamanio = item_senial_adquirida.getElementsByTagName("tamanio")[0]
        # Llena la lista con los parametros asociados a la senial
        tamanio = item_tamanio.firstChild.data.strip()
        # Crea el procesador
        return FactorySenial.obtener_senial(senial, tamanio)
    except Exception as ex:
        raise ex


def definir_procesador():
    """
    Recupera desde la configuración el tipo de procesador y los
    parametros asociado
    Luego llama la factory para que devuelva el tipo de procesador creado
    """
    try:
        # Parsea el xml de configuracion
        conf_procesador = minidom.parse("./datos/configuracion.xml")
        # Busca el nodo del procesador
        item_procesador = conf_procesador.getElementsByTagName("procesador")[0]
        # Obtiene el nombre del tipo de procesador definido
        procesador = item_procesador.firstChild.data.strip()
        # Busca los nodos de los parametros
        item_params = item_procesador.getElementsByTagName("param")
        # Llena la lista con los parametros asociados al procesador
        params = []
        for param in item_params:
            params.append(param.firstChild.data)
        # Crea el procesador
        return FactoryProcesador.obtener_procesador(procesador,
                                                    definir_senial_procesar(),
                                                    params)
    except Exception as ex:
        raise ex


def definir_adquisidor():
    """
    Recupera desde la configuración el tipo de adquisidor y los
    parametros asociado
    Luego llama la factory para que devuelva el tipo de adquisidor creado
    """
    try:
        # Parsea el xml de configuracion
        conf_adquisidor = minidom.parse("./datos/configuracion.xml")
        # Busca el nodo del adquisidor
        item_adquisidor = conf_adquisidor.getElementsByTagName("adquisidor")[0]
        adquisidor = item_adquisidor.firstChild.data.strip()
        # Busca los nodos de los parametros
        item_params = item_adquisidor.getElementsByTagName("param")
        # Llena la lista con los parametros asociados al procesador
        params = []
        for param in item_params:
            params.append(param.firstChild.data)
        # Crea el procesador
        return FactoryAdquisidor.obtener_adquisidor(adquisidor,
                                                    definir_senial_adquirir(),
                                                    params)
    except Exception as ex:
        raise ex


def definir_visualizador():
    return Visualizador()


def definir_contexto(recurso):
    return ContextoPickle(recurso)


def definir_repositorio(contexto):
    return RepositorioSenial(contexto)


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
