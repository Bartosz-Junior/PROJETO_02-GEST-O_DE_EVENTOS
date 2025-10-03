from .eventos import Evento
from utils import helpers_functions, db_functions
import datetime, json


class Workshop(Evento):
    def __init__(self, nome, data_evento, local, capacidade_max, numero_inscritos, categoria, preco_ingresso):
        super().__init__(nome, data_evento, local, capacidade_max, categoria, numero_inscritos, preco_ingresso)        
        self._data_atual = datetime.datetime.today()

    def salvar_workshop(self):

        dados_workshop = {
            "Tema" : self.nome,
            "Data" : self.data_evento,
            "Local" : self.local_evento,
            "Capacidade_max" : self.capacidade_max, 
            "Numero_inscritos" : self.numero_inscritos,
            "Categoria" : self.categoria,
            "Preço ingresso" : self.preco_ingresso
        }
        
        carrega_palestras = db_functions.carregar_json("database/workshops.json")
        carrega_palestras.append(dados_workshop)
        
        with open("database/palestras.json", "w", encoding= "utf-8") as file:
            json.dump(carrega_palestras, file, indent= 4, ensure_ascii= False)
            
    def listar_workshop(self):
        carrega_workshop = db_functions.carregar_json("database\wokshops.json")
        for i,v in enumerate(carrega_workshop):
            print(f"_____ WORKSHOP {i + 1} _____")
            print(f"Tema: {v["Tema"]:5}")
            print(f"Data: {v["Data"]:5}")
            print(f"Local: {v["Local"]:5}")
            print(f"Capacidade: {v["Capacidade_max"]:5}")
            print(f"Categoria: {v["Categoria"]:5}")
            print(f"Preço: R${v["Preço ingresso"]:5.2f}\n")
