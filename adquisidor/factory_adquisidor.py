"""
Fabrica de tipos de adquisidor
"""
from adquisidor.adquisidor import *

class FactoryAdquisidor(object):
    '''
    Se propone que esta clase no necesariamente sea intanciada, ya que no se
    necesita. Con solo una instancia de fabricacion es suficiente y por otro
    lado no se precisa de mantener ningun estado.
    '''

    @staticmethod
    def obtener_adquisidor(tipo_adquisidor, senial, params):
        '''
        Metodo que crea una instancia del tipo adquisidor
        :param tipo_adquisidor: nombre del tipo de adquisidor
        :param senial: tipo de señal que se le asigna al adquisidor
        :param params: parametros relacionados con el tipo adquisidor
        :return:
        '''
        adquisidor = None
        if tipo_adquisidor == 'simple':
            adquisidor = AdquisidorSimple(senial)

        elif tipo_adquisidor == 'archivo':
            ubicacion = str(params[0])
            adquisidor = AdquisidorArchivo(senial, ubicacion)

        elif tipo_adquisidor == 'senoidal':
            adquisidor = AdquisidorSenoidal(senial)

        return adquisidor