from utils import db_functions


class Participante:
    def __init__(self, nome, email, evento_escolhido, checkin=False):
        self._nome = nome
        self._email = email
        self._evento = evento_escolhido
        self._checkin = checkin

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def evento(self):
        return self._evento
    
    @property
    def checkin(self):
        return self._checkin
    
    @checkin.setter
    def checkin(self, valor):
        self._checkin = valor
    
    def salvar_participante_json(self, diretorio):

        dict_participante = {
            "nome" : self.nome,
            "email" : self.email,
            "evento_escolhido" : self.evento,
            "checkin" : self.checkin
        }

        dados = db_functions.carregar_json(diretorio)
        dados.append(dict_participante)
        db_functions.salvar_json(diretorio, dados)
    
    def verificar_email(self, diretorio):
        dados = db_functions.carregar_json(diretorio)

        for dado in dados:
            if dado["email"] == self.email:
                print(f"O e-mail: {self.email} já está cadastrado!")
                return True

    def remover_inscrito(self):
        dados = db_functions.carregar_json("database/participantes.json")

        for dado in dados:
            if dado["email"] == self.email:
                dados.remove(dado)
                db_functions.salvar_json("database/participantes.json", dados)
                print("Participante excluido do sistema")
                return self.evento

    def fazer_checkin(self):
        if self.checkin == True:
            print(f"{self.nome} já fez check-in.")
            return

        self.checkin = True
        dados = db_functions.carregar_json("database/participantes.json")

        for dado in dados:
            if dado["nome"] == self.nome:
                dado["checkin"] = self.checkin
                print(f"Check-in realizado com sucesso para {self.nome}")
        db_functions.salvar_json("database/participantes.json", dados)
        

    def __str__(self):
        return f"{self._nome}, {self._email}, {self._evento}, {self._checkin}"