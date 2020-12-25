import unittest2

from ejercicio2 import *


class Pruebas(unittest2.TestCase):
    def test_validar_edad(self):
        self.assertIsNot(edad, self)


#        self.assertIsInstance(peso,sexo)

if __name__ == "__main__":
    unittest2.main()
