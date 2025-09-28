from .eventos import Evento
import json

class Palestra(Evento):
    def __init__(self, nome = None, data_evento= None, local = None, capacidade_max = None, num_inscritos = None, categoria = None, preco_ingresso = None):
        super().__init__(nome, data_evento, local, capacidade_max, num_inscritos, categoria, preco_ingresso)
    
    def add_evento(self):
        return super().add_evento()

    def listar_palestras(self):
        print("__________ PALESTRAS DISPONIVEIS __________" )
        with open("C:/Users/Júnior/Documents/Projeto_02_BFD/PROJETO_02-GEST-O_DE_EVENTOS/database/palestras.json", "r", encoding= "utf-8") as file:
            carrega_palestras = json.load(file)
            for i,v in enumerate(carrega_palestras):
                print(f"{i + 1:}- Tema: {v["Tema"]:5} Data: {v["Data"]:5} Local: {v["Local"]:5} Capacidade: {v["Capacidade"]:5} Categoria: {v["Categoria"]:5} Preço: R${v["Preço ingresso"]:5.2f}\n")
