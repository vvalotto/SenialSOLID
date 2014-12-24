"""
Modulo que define la entidad Senial.
Es considerada una entidad del dominio

Modificacion: Se crea un clase abstracta que define todas las interfaces de las
estructuras de las seniales y resuelve la violacion de los principio OCP y LSP
"""


from abc import ABCMeta, abstractmethod
from collections import deque


class SenialBase(metaclass=ABCMeta):
    """
    Definición de la entidad tipo Senial.
    En este caso es una definicion de una clase concreta.
    Tiene las funciones:
    -> poner_valor(valor)
    -> obtener_valot(indice)
    -> obtener_tamanio()
    """
    def __init__(self, tamanio=10):
        """
        Constructor: Inicializa la lista de valores vacia
        :return:
        """
        self._valores = []
        self._fecha_adquisicion = None
        self._tamanio = tamanio
        self._cantidad = 0
        return

    # Propiedades
    # Fecha de Adquisicion
    @property
    def fecha_adquisicion(self):
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor):
        self._fecha_adquisicion = valor

    @fecha_adquisicion.deleter
    def fecha_adquisicion(self):
        del self._fecha_adquisicion

    # Cantidad da datod de la adquisicion
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor

    # Tamanio de la estructura que mantiene los datos
    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor):
        self._tamanio = valor

    # Valores de las seniales
    @property
    def valores(self):
        return self._valores

    @valores.setter
    def valores(self, datos):
        self._valores = datos

    @abstractmethod
    def poner_valor(self, valor):
        pass

    @abstractmethod
    def sacar_valor(self, *valor):
        pass

    def limpiar(self):
        """
        Deja a la senial sin valores
        """
        self._valores.clear()
        self._cantidad = 0

    def obtener_valor(self, indice):
        """
        Devuelve el valor contenido en la lista de acuerdo a al indice
        :param indice:
        :return: valor
        """
        try:
            valor = self._valores[indice]
            return valor
        except Exception as ex:
            print("Error ", ex)
            return None

    def __str__(self):
        cad = ""
        cad += "tamanio: " + str(self._tamanio) + "\n"
        cad += "fecha_adquisicion: " + str(self._fecha_adquisicion)
        return cad


class Senial(SenialBase):
    """
    Clase tipo lista que implementa los metodos de manipulacion de datos
    dentro de la estructura
    """
    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        if self._cantidad < self._tamanio:
            self._valores.append(valor)
            self._cantidad += 1
        else:
            raise Exception('No se pueden poner mas datos')
        return

    def sacar_valor(self):
        valor = 0
        try:
            valor = self._valores.pop()
            self._cantidad -= 1
        except Exception as ex:
            print('Error: No hay nada para sacar')
        return valor


class SenialPila(SenialBase):

    def poner_valor(self, valor):
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        if self._cantidad < self._tamanio:
            self._valores.append(valor)
            self._cantidad += 1
        else:
            raise Exception('No se pueden poner mas datos')
        return

    def sacar_valor(self):
        valor = 0
        try:
            valor = self._valores.pop()
            self._cantidad -= 1
        except Exception as ex:
            print('Error: No hay nada para sacar')
        return valor


class SenialCola(SenialBase):
    def __init__(self, tamanio):
        super().__init__(tamanio)
        self._valores = deque([])

    def poner_valor(self, valor):
        if self._cantidad < self._tamanio:
            self._valores.append(valor)
            self._cantidad += 1
        else:
            raise Exception('No se pueden poner mas datos')
        return

    def sacar_valor(self):
        valor = 0
        try:
            valor = self._valores.popleft()
            self._cantidad -= 1
        except Exception as ex:
            print('No hay nada para sacar:', ex)
        return valor