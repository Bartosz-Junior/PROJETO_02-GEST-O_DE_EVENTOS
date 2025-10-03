from .eventos import Evento
from utils import db_functions
import json, datetime

class Palestra(Evento):
    def __init__(self, nome, data_evento, local, capacidade_max, numero_inscritos, categoria, preco_ingresso):
        super().__init__(nome, data_evento, local, capacidade_max, numero_inscritos, categoria, preco_ingresso)

        self._data_atual = datetime.datetime.today()

    
    def salvar_palestra(self):

        dados_palestra = {
            "Tema" : self.nome,
            "Data" : self.data_evento,
            "Local" : self.local_evento,
            "Capacidade_max" : self.capacidade_max, 
            "Numero_inscritos" : self.numero_inscritos,
            "Categoria" : self.categoria,
            "Preço ingresso" : self.preco_ingresso
        }
        
        carrega_palestras = db_functions.carregar_json("database/palestras.json")
        carrega_palestras.append(dados_palestra)
        
        with open("database/palestras.json", "w", encoding= "utf-8") as file:
            json.dump(carrega_palestras, file, indent= 4, ensure_ascii= False)

    def listar_palestras(self):
        carrega_palestras = db_functions.carregar_json("database/palestras.json")
        for i,v in enumerate(carrega_palestras):
            print(f"_____ PALESTRA {i + 1} _____")
            print(f"Tema: {v["Tema"]:5}")
            print(f"Data: {v["Data"]:5}")
            print(f"Local: {v["Local"]:5}")
            print(f"Capacidade: {v["Capacidade_max"]:5}")
            print(f"Categoria: {v["Categoria"]:5}")
            print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")
