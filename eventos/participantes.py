from eventos.palestra import Palestra
from eventos.workshop import Workshop
import json
import os

class Participante:
    def __init__(self, nome, email, evento_escolhido):
        self._nome = nome
        self._email = email
        self._evento = evento_escolhido

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def evento(self):
        return self._evento
    
    def gerar_dict(self):

        return {
            "nome" : self.nome,
            "email" : self.email,
            "evento_escolhido" : self.evento
        }

    def __str__(self):
        return f"{self._nome} <{self._email}> <{self._evento}>"