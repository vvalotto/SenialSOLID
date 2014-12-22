"""
Modulo que define la entidad Senial.
Es considerada una entidad del dominio

Modificacion: Se agregan miembros de instancias y se definen como propiedades
"""


class Senial(object):
    """
    Definicion de la entidad tipo Senial.
    En este caso es una definicion de una clase concreta.
    Tiene las funciones:
    -> poner_valor(valor)
    -> obtener_valor(indice)
    -> obtener_tamanio()
    -> obtener_tamanio()
    """
    
    def __init__(self):
        """
        Constructor: Inicializa la lista de valores vacia
        :return:
        """
        self._valores = []
        self._fecha_adquisicion = None
        self._cantidad = 0
        return

    #Propiedades
    #Fecha de Adquisicion
    @property
    def fecha_adquisicion(self):
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor):
        self._fecha_adquisicion = valor

    @fecha_adquisicion.deleter
    def fecha_adquisicion(self):
        del self._fecha_adquisicion

    #Tamanio de la adquisicion
    @property
    def tamanio(self):
        return self._cantidad

    @tamanio.setter
    def tamanio(self, valor):
        self._cantidad = valor

    @property
    def valores(self):
        return self._valores

    @valores.setter
    def valores(self, datos):
        self._valores = datos


    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        self._valores.append(valor)
        self._cantidad += 1
        return
    
    def obtener_valor(self, indice):
        """
        Recupera el contenido según el indice
        :param indice:
        :return: Valor
        """
        try:
            valor = self._valores[indice]
            return valor
        except Exception as ex:
            print('Error: ', ex.args)
            return None
