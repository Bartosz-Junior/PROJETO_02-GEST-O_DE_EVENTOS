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
    
    def salvar_participante(self, dados_participante, evento_escolhido):
        with open("database/participantes.json", "r", encoding= "utf-8") as file:
            carrega_participantes = json.load(file)
            carrega_participantes.append(dados_participante)
                    
        with open("database/participantes.json", "w", encoding= "utf-8") as file:
            json.dump(carrega_participantes, file, indent= 4, ensure_ascii= False)

        evento_escolhido.adicionar_inscrito()

    def __str__(self):
        return f"{self._nome} <{self._email}> <{self._evento}>"