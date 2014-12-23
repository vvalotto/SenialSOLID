import unittest
from modelo.senial import *


class TestSenial(unittest.TestCase):
    def setUp(self):
        self.senial = Senial()
        self.senialpila = SenialPila()
        self.senialcola = SenialCola(10)

    def test_poner_valor(self):
        self.senial.poner_valor(10)
        self.assertEqual(10, self.senial._valores[0])

    def test_obtener_valor(self):
        self.senial.poner_valor(10)
        self.assertEqual(10, self.senial.obtener_valor(0))

    def test_es_pila(self):
        self.assertTrue(isinstance(self.senialpila, SenialPila))

    def test_es_cola(self):
        self.assertTrue(isinstance(self.senialcola, SenialCola))

    def test_es_lista(self):
        self.assertTrue(isinstance(self.senialcola, Senial))

    def test_es_no_lista(self):
        self.assertTrue(not isinstance(self.senial, SenialPila))

    def test_es_no_lista2(self):
        self.assertTrue(not isinstance(self.senial, SenialCola))

    def test_llena_lista(self):
        self.senial.tamanio = 5
        for i in range(0, 5):
            self.senial.poner_valor(i * 10)
        self.assertEqual([0, 10, 20, 30, 40], self.senial._valores)
        self.assertEqual(4, self.senial.cantidad)

if __name__ == '__main__':
    unittest.main()