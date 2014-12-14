"""
Define la clase procesador de la senail
"""
from modelo.senial import Senial


class Procesador(object):
    """
    Constructor: Inicializa la senial que resultara procesada.
    """
    def __init__(self):
        self._senial_procesada = Senial()
        return
    
    def procesar_senial(self, senial):
        """
        Metodo que realiza el procesamiento de la senial
        :param senial: a procesar
        :return:
        """
        print("Procesando...")
        for i in range(0, senial.obtener_tamanio()):
            self._senial_procesada.poner_valor(senial.obtener_valor(i) * 2)
        return
    
    def obtener_senial_procesada(self):
        """
        Devuelve la senial procesada
        :return:
        """
        return self._senial_procesada