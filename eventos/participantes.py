class Participante:
    def __init__(self, nome, email, evento_escolhido):
        self.nome = nome
        self.email = email
        self.evento = evento_escolhido

    def exibir_participante(self):
        return f"{self.nome} <{self.email}> <{self.evento}>"