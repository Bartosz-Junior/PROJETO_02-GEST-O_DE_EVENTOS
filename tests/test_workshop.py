import unittest
from eventos.workshop import Workshop

class TestWorkshop(unittest.TestCase):
    def setUp(self):
        self.workshop = Workshop("Introdução a IA", "09/10/2025", "São Paulo", 50, 5, "Inovação", "workshop", 100.0)

    def test_criacao_workshop(self):
        self.assertEqual(self.workshop.tema, "Introdução a IA")
        self.assertEqual(self.workshop.tipo, "workshop")

    def test_vagas_disponiveis(self):
        self.assertTrue(self.workshop.numero_inscritos < self.workshop.capacidade_max)
