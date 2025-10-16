import unittest
from unittest.mock import patch
from io import StringIO
from utils.helpers_functions import listar_dados


class TestListarDados(unittest.TestCase):

    def test_lista_vazia(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            listar_dados([], "palestras")
            saida = mock_stdout.getvalue()
            self.assertIn("Nenhum palestras cadastrado ainda", saida)

    def test_lista_com_dados(self):
        dados = [
            {"tema": "Python Básico", "data": "10/10/2025", "local": "Online"},
            {"tema": "IA na prática", "data": "15/10/2025", "local": "SP"}
        ]

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            listar_dados(dados, "palestras")
            saida = mock_stdout.getvalue()
            self.assertIn("LISTA DE PALESTRAS", saida)
            self.assertIn("Python Básico", saida)
            self.assertIn("IA na prática", saida)

if __name__ == "__main__":
    unittest.main()
