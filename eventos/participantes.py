from utils import db_functions


class Participante:
    def __init__(self, nome, email, evento_escolhido):
        self._nome = nome
        self._email = email
        self._evento = evento_escolhido

    diretorio = "database/participantes.json"

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def evento(self):
        return self._evento
    
    def salvar_participante_json(self, diretorio):

        dict_participante = {
            "nome" : self.nome,
            "email" : self.email,
            "evento_escolhido" : self.evento
        }

        dados = db_functions.carregar_json(diretorio)
        dados.append(dict_participante)
        db_functions.salvar_json(diretorio)
    
    def verificar_email(self, diretorio):
        dados = db_functions.carregar_json(diretorio)

        for dado in dados:
            if dado["email"] == self.email:
                print(f"O e-mail: {self.email} já está cadastrado!")
                return True

    def cancelar_inscricao(self):
        pass

    def __str__(self):
        return f"{self._nome} <{self._email}> <{self._evento}>"