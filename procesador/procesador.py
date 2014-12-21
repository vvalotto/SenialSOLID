from modelo.senial import Senial


class Procesador(object):
    """
    Define la clase procesador de la senial
    """

    def __init__(self):
        """
        Constructor: Inicializa la senial que resultara procesada.
        """
        self._senial_procesada = Senial()
        self._umbral = 0
        return
    
    def procesar_senial(self, senial):
        """
        Metodo que realiza el procesamiento de la senial
        :param senial: a procesar
        :return:
        """
        print("Procesando...")
        self._senial_procesada._valores = list(map(self.funcion_doble, senial._valores))
        return

    def procesar_senial_con_umbral(self, senial, umbral=10):
        """
        Metodo que realiza el procesamiento de la senial con umbral
        :param senial: a procesar
        :return:
        """
        self._umbral = umbral
        print("Procesando con umbral")
        self._senial_procesada._valores = list(map(self.funcion_umbral, senial._valores))
        return

    def obtener_senial_procesada(self):
        """
        Devuelve la senial procesada
        :return:
        """
        return self._senial_procesada

    @staticmethod
    def funcion_doble(valor):
        """
        Funcion que retorna el doble de valor de entrada
        :param valor:
        :return:
        """
        return valor * 2


    def funcion_umbral(self, valor):
        """
        Funcion que filtra valores con un umbral
        :param valor:
        :return:
        """
        return valor if valor < self._umbral else 0