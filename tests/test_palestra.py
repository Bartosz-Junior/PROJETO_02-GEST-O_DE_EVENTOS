import unittest
from eventos.palestra import Palestra

class TestPalestra(unittest.TestCase):
    def setUp(self):
        self.palestra = Palestra("Python Avançado", "10/10/2025", "Online", 100, 10, "Tecnologia", "palestra", 50.0)

    def test_criacao_palestra(self):
        self.assertEqual(self.palestra.tema, "Python Avançado")
        self.assertEqual(self.palestra.local, "Online")
        self.assertEqual(self.palestra.tipo, "palestra")

    def test_reducao_inscritos(self):
        inscritos_iniciais = self.palestra.numero_inscritos
        self.palestra.reduzir_numero_inscritos()
        self.assertEqual(self.palestra.numero_inscritos, inscritos_iniciais - 1)