import unittest
from unittest.mock import patch
from io import StringIO
from utils.helpers_functions import buscar_eventos

class TestBuscarEventos(unittest.TestCase):

    @patch("builtins.input", side_effect=["palestras", "10/10/2025", "tech"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_buscar_eventos_encontrado(self, mock_stdout, mock_input):
        dict_dados = {
            "palestras": [
                {"tema": "Python Avançado", "data": "10/10/2025", "categoria": "tech"},
                {"tema": "Marketing Digital", "data": "15/11/2025", "categoria": "negocios"}
            ],
            "workshops": []
        }

        buscar_eventos(dict_dados)

        saida = mock_stdout.getvalue()
        self.assertIn("Total de 1 encontrados", saida)
        self.assertIn("Python Avançado", saida)


    @patch("builtins.input", side_effect=["workshops", "01/01/2024", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_buscar_eventos_sem_resultados(self, mock_stdout, mock_input):
        dict_dados = {
            "palestras": [],
            "workshops": [{"tema": "Data Science", "data": "10/10/2025", "categoria": "tech"}]
        }

        buscar_eventos(dict_dados)
        saida = mock_stdout.getvalue()

        self.assertIn("Total de 0 eventos encontrados", saida)


    @patch("builtins.input", side_effect=["filme", "palestras", "", ""])
    @patch("sys.stdout", new_callable=StringIO)
    def test_buscar_eventos_tipo_invalido(self, mock_stdout, mock_input):
        dict_dados = {"palestras": [], "workshops": []}

        buscar_eventos(dict_dados)
        saida = mock_stdout.getvalue()

        self.assertIn("Tipo invalido", saida)


if __name__ == "__main__":
    unittest.main()
