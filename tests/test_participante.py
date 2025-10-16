import unittest
from unittest.mock import patch
from eventos.participantes import Participante


class TestParticipante(unittest.TestCase):

    def setUp(self):
        self.participante = Participante(
            nome="João Silva",
            email="joao@email.com",
            evento_escolhido="Workshop Python",
            checkin=False
        )

    def test_atributos_iniciais(self):
        self.assertEqual(self.participante.nome, "João Silva")
        self.assertEqual(self.participante.email, "joao@email.com")
        self.assertEqual(self.participante.evento, "Workshop Python")
        self.assertFalse(self.participante.checkin)

    def test_checkin_setter_funciona(self):
        self.participante.checkin = True
        self.assertTrue(self.participante.checkin)

    @patch("utils.db_functions.carregar_json", return_value=[])
    @patch("utils.db_functions.salvar_json")
    def test_salvar_participante_json(self, mock_salvar, mock_carregar):
        self.participante.salvar_participante_json("database/participantes.json")
        mock_carregar.assert_called_once()
        mock_salvar.assert_called_once()

    @patch("utils.db_functions.carregar_json", return_value=[{"email": "joao@email.com"}])
    def test_verificar_email_existente(self, mock_carregar):
        existe = self.participante.verificar_email("database/participantes.json")
        self.assertTrue(existe)

    @patch("utils.db_functions.carregar_json", return_value=[{"email": "joao@email.com"}])
    @patch("utils.db_functions.salvar_json")
    def test_remover_inscrito(self, mock_salvar, mock_carregar):
        retorno = self.participante.remover_inscrito()
        self.assertEqual(retorno, "Workshop Python")
        mock_salvar.assert_called_once()

    @patch("utils.db_functions.carregar_json", return_value=[
        {"nome": "João Silva", "email": "joao@email.com", "checkin": False}
    ])
    
    @patch("utils.db_functions.salvar_json")
    def test_fazer_checkin(self, mock_salvar, mock_carregar):
        self.participante.fazer_checkin()
        self.assertTrue(self.participante.checkin)
        mock_salvar.assert_called_once()


if __name__ == "__main__":
    unittest.main()
