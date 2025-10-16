import unittest
import json
import os
from utils import db_functions

class TestDBFunctions(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.json"
        self.data = [{"tema": "Python", "numero_inscritos": 10}]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_salvar_e_carregar_json(self):
        db_functions.salvar_json(self.test_file, self.data)
        loaded = db_functions.carregar_json(self.test_file)
        self.assertEqual(loaded[0]["tema"], "Python")

    def test_carregar_objeto(self):
        from eventos.palestra import Palestra
        dado = {
            "tema": "Flask",
            "data": "10/10/2025",
            "local": "Online",
            "capacidade_max": 100,
            "numero_inscritos": 10,
            "categoria": "Web",
            "tipo": "palestra",
            "preco_ingresso": 0
        }
        objeto = db_functions.carregar_objeto(dado, Palestra)
        self.assertEqual(objeto.tema, "Flask")
